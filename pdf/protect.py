import PyPDF2
import sys


def create_pass_protected_pdf(inp_file,out_file,password):
    try:
        with open(inp_file, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_writer = PyPDF2.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            pdf_writer.encrypt(password)

            with open(out_file, "wb") as output_file:
                pdf_writer.write(output_file)

            print(f"Output PDF saved as {out_file}")

    except FileNotFoundError:
        print(f"The file {inp_file} not found")

    except PyPDF2.utils.PdfReadError:
        print(f"Error reading the PDF file {inp_file}. It may be corrupted or not a valid PDF.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python protect.py <input.pdf> <output.pdf> <password>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    password = sys.argv[3]

    create_pass_protected_pdf(input_file, output_file, password)

if __name__ == "__main__":
    main()




# if len(sys.argv) != 3:
#     print("Usage: python protect.py <input.pdf> <output.pdf>")
#     sys.exit(1)

# input_file = sys.argv[1]
# output_file = sys.argv[2]

# with open(input_file, "rb") as f:
#     pdf_reader = PyPDF2.PdfReader(f)
#     pdf_writer = PyPDF2.PdfWriter()

#     for page in pdf_reader.pages:
#         pdf_writer.add_page(page)

#     with open(output_file, "wb") as f:
#         pdf_writer.write(f)

# def create_password_protected_pdf(input_file, output_file, password):
#     with open(input_file, "rb") as f:
#         pdf_reader = PyPDF2.PdfReader(f)
#         pdf_writer = PyPDF2.PdfWriter()

#         for page in pdf_reader.pages:
#             pdf_writer.add_page(page)

#         pdf_writer.encrypt(password)

#         with open(output_file, "wb") as f:
#             pdf_writer.write(f)

# create_password_protected_pdf("inp.pdf", "out.pdf", "password")
