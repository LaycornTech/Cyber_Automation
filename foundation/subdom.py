import requests
import threading

from tqdm import tqdm

domain = "youtube.com"

with open("subdomains.txt") as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock()

def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)

    except requests.ConnectionError:
        pass
    else:
        print(f"[+] Discovered subdomain: {url}")
        with lock:
            discovered_subdomains.append(url)

threads = []

for subdomain in subdomains:
    thread = threading.Thread(target = check_subdomain, args = (subdomain, ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# def time_download():
#     with open("discovered_subdomains", "w") as f:
#         for subdomain in tqdm(range(100), desc="Downloading discovered subdomains"):
#             print(subdomain, file = f)
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in tqdm(discovered_subdomains, desc="Saving discovered subdomains"):
        print(subdomain, file = f)
# with open("discovered_subdomains.txt", "w") as f:
#     for subdomain in discovered_subdomains:
#         print(subdomain, file = f)

