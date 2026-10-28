import concurrent.futures
import urllib.request
import urllib.error

# 1. Define the function that does the heavy lifting (I/O bound task)
def check_website(url):
    try:
        # We add a 5-second timeout so it doesn't hang forever
        with urllib.request.urlopen(url, timeout=5) as response:
            return f"Status {response.status} (OK)"
    except urllib.error.URLError as e:
        return f"Failed to connect ({e.reason})"
    except Exception as e:
        return f"Error: {str(e)}"

# 2. List of websites to check concurrently
websites = [
    "https://google.com",
    "https://github.com",
    "https://python.org",
    "https://this-is-a-broken-website-url.com",  # Will fail
]

# 3. Use ThreadPoolExecutor to run them in parallel
print("Starting concurrent website check...\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # --- HERE IS THE DICTIONARY COMPREHENSION ---
    # We map each Future object (key) to its corresponding URL (value)
    future_to_url = {executor.submit(check_website, url): url for url in websites}
    
    # 4. Process results asynchronously as they finish
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future] # Retrieve the original URL using the Future key
        try:
            result = future.result() # Get the returned string from check_website()
            print(f"[+] {url} -> {result}")
        except Exception as exc:
            print(f"[X] {url} generated an unexpected exception: {exc}")

print("\nAll checks completed!")
