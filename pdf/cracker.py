import itertools
import pikepdf
from tqdm import tqdm
import concurrent.futures
import argparse


# def generate_passwords(characters, length):
#     """Generate all possible passwords of a given length using the specified characters."""
#     return (''.join(candidate) for candidate in itertools.product(characters, repeat=length))


# print(len(list(generate_passwords("abc", 3))))  # Example usage: generates 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'


def load_wordlist(wordlist_file):
    """Load a wordlist from a file and return a list of words."""
    # with open(wordlist_file, 'r', encoding='utf-8') as f:
    #     return [line.strip() for line in f if line.strip()]

    with open(wordlist_file, "r") as file:
        for line in file:
            yield line.strip()

def try_password(pdf_file, password):
    """Try to open the PDF file with the given password."""
    # try:
    #     with pikepdf.open(pdf_file, password=password):
    #         return True
    # except pikepdf._qpdf.PasswordError:
    #     return False
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            print(f"[+] Password found: {password}")
            return password
        
    except pikepdf._core.PasswordError:
        return None


def decrypt_pdf(pdf_file, total_passwords, passwords, max_workers= 4):
    with tqdm(total = total_passwords, desc = "DEcrypting PDF", unit = "passwords") as pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_password = {executor.submit(try_password, pdf_file, pwd): pwd for pwd in passwords}

            for future in future_to_password:
                password = future_to_password[future]

                if future.result():
                    return future.result()  # Return the found password
                pbar.update(1)


    print("Unable to decrypt PDF. Password not found.")

    return None



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Password Cracker")
    parser.add_argument("pdf_file", help="Path to the password protected PDF file")
    parser.add_argument("-w", "--wordlist", help="Path to the Password list file", default=None)
    parser.add_argument("-min", "--min_length", type=int, default=1, help="Minimum password length to generate for brute force")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate password on the fly")
    parser.add_argument("-max", "--max_length", type=int, default=4, help="Maximum password length to generate for brute force")
    parser.add_argument("-c", "--chars", default="abcdefghijklmnopqrstuvwxyz0123456789", help="Characters to use for brute force")
    parser.add_argument("--max_workers", type=int, default=4, help="Maximum number of worker threads to use")


    
    args = parser.parse_args()

    if args.generate:
        passwords = generate_passwords(args.chars, args.min_length, args.max_length)
        total_passwords = sum(1 for _ in generate_passwords(args.chars, args.min_length, args.max_length))

    elif args.wordlist:
        passwords = load_wordlist(args.wordlist)
        total_passwords = sum(1 for _ in load_wordlist(args.wordlist))

    else:
        print("Please provide either a wordlist or specify the characters and length for brute force.")
        exit(1)

    decrypted_password = decrypt_pdf(args.pdf_file, total_passwords, passwords, max_workers=args.max_workers)

    if decrypted_password:
        print(f"[+] Password found: {decrypted_password}")
    else:
        print("[-] Password not found.")


















































# def decrypt_pdf(pdf_file, password):
#     """Decrypt the PDF file using the provided password."""
#     try:
#         with pikepdf.open(pdf_file, password=password) as pdf:
#             decrypted_pdf_path = f"decrypted_{pdf_file}"
#             pdf.save(decrypted_pdf_path)
#             print(f"[+] Decrypted PDF saved as: {decrypted_pdf_path}")
#             return decrypted_pdf_path
#     except pikepdf._core.PasswordError:
#         print("[-] Failed to decrypt PDF. Incorrect password.")
#         return None

# def crack_pdf(pdf_file, wordlist_file):
#     """Attempt to crack the PDF password using a wordlist."""
#     for password in load_wordlist(wordlist_file):
#         if try_password(pdf_file, password):
#             return password
#     return None

# def crack_pdf_with_bruteforce(pdf_file, chars, min_length, max_length):
#     """Attempt to crack the PDF password using brute force."""
#     for password in generate_passwords(chars, min_length, max_length):
#         if try_password(pdf_file, password):
#             return password
#     return None            

# def main():
#     pdf_file = "protected.pdf"  # Replace with your PDF file path
#     wordlist_file = "wordlist.txt"  # Replace with your wordlist file path

#     print("[*] Starting wordlist attack...")
#     password = crack_pdf(pdf_file, wordlist_file)
#     if password:
#         print(f"[+] Password found using wordlist: {password}")
#     else:
#         print("[-] Password not found in wordlist. Starting brute force attack...")
#         chars = "abcdefghijklmnopqrstuvwxyz0123456789"  # Characters to use for brute force
#         min_length = 1
#         max_length = 4  # Adjust as needed
#         password = crack_pdf_with_bruteforce(pdf_file, chars, min_length, max_length)
#         if password:
#             print(f"[+] Password found using brute force: {password}")
#         else:
#             print("[-] Password not found using brute force.")  



# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="PDF Password Cracker")
#     parser.add_argument("pdf_file", help="Path to the PDF file")
#     parser.add_argument("wordlist_file", help="Path to the wordlist file")
#     parser.add_argument("--min_length", type=int, default=1, help="Minimum password length for brute force")
#     parser.add_argument("--max_length", type=int, default=4, help="Maximum password length for brute force")
#     parser.add_argument("--chars", default="abcdefghijklmnopqrstuvwxyz0123456789", help="Characters to use for brute force")

#     args = parser.parse_args()

#     pdf_file = args.pdf_file
#     wordlist_file = args.wordlist_file
#     min_length = args.min_length
#     max_length = args.max_length
#     chars = args.chars

#     print("[*] Starting wordlist attack...")
#     passwords_from_wordlist = load_wordlist(wordlist_file)
#     total_passwords_wordlist = sum(1 for _ in load_wordlist(wordlist_file))  # Count total passwords in wordlist
#     found_password = decrypt_pdf(pdf_file, total_passwords_wordlist, passwords_from_wordlist)

#     if found_password:
#         print(f"[+] Password found using wordlist: {found_password}")
#     else:
#         print("[-] Password not found in wordlist. Starting brute force attack...")
#         passwords_from_bruteforce = generate_passwords(chars, min_length, max_length)
#         total_passwords_bruteforce = sum(1 for _ in generate_passwords(chars, min_length, max_length))  # Count total passwords for brute force
#         found_password = decrypt_pdf(pdf_file, total_passwords_bruteforce, passwords_from_bruteforce)

#         if found_password:
#             print(f"[+] Password found using brute force: {found_password}")
#         else:
#             print("[-] Password not found using brute force.")     


# args = parser.parse_args()
#     if args.generate:
#         print(f"[*] Starting brute force attack on {args.pdf_file}...")
#         passwords = generate_passwords(args.chars, args.min_length, args.max_length)
#         total_passwords = sum(1 for _ in generate_passwords(args.chars, args.min_length, args.max_length))
#         found_password = decrypt_pdf(args.pdf_file, total_passwords, passwords, max_workers=args.max_workers)
#         if found_password:
#             print(f"[+] Password found using brute force: {found_password}")
#         else:
#             print("[-] Password not found using brute force.")
#     elif args.wordlist:
#         print(f"[*] Starting wordlist attack on {args.pdf_file} using {args.wordlist}...")
#         passwords = load_wordlist(args.wordlist)
#         total_passwords = sum(1 for _ in load_wordlist(args.wordlist))
#         found_password = decrypt_pdf(args.pdf_file, total_passwords, passwords, max_workers=args.max_workers)
#         if found_password:
#             print(f"[+] Password found using wordlist: {found_password}")
#         else:
#             print("[-] Password not found in wordlist.")    
            

