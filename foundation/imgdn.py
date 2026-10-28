import concurrent.futures
import os
import urllib.request

# 1. Define the worker function that downloads a single image
def download_image(url, save_path):
    try:
        # Define a standard user-agent header to avoid getting blocked by some websites
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(save_path, 'wb') as f:
                f.write(response.read())
        return f"Successfully downloaded to {save_path}"
    except Exception as e:
        return f"Failed to download: {str(e)}"

# 2. Setup a target directory and sample image URLs
output_dir = "downloaded_images"
os.makedirs(output_dir, exist_ok=True)

# A dictionary mapping URLs to what we want to name the final local files
images_to_download = {
    "https://picsum.photos": os.path.join(output_dir, "photo_1.jpg"),
    "https://picsum.photos": os.path.join(output_dir, "photo_2.jpg"),
    "https://picsum.photos": os.path.join(output_dir, "photo_3.jpg"),
    "https://picsum.photos": os.path.join(output_dir, "photo_4.jpg"),
}

print("Starting concurrent image downloads...\n")

# 3. Use ThreadPoolExecutor to run downloads in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    
    # --- YOUR DICTIONARY COMPREHENSION ---
    # We submit each task and map the resulting Future key to the local file path value
    future_to_filepath = {
        executor.submit(download_image, url, path): path 
        for url, path in images_to_download.items()
    }
    
    # 4. As each download finishes, grab the result immediately
    for future in concurrent.futures.as_completed(future_to_filepath):
        file_path = future_to_filepath[future] # Look up the file path using the Future key
        try:
            status_message = future.result() # Get the return string from download_image()
            print(f"[+] {status_message}")
        except Exception as exc:
            print(f"[X] {file_path} threw an unexpected exception: {exc}")

print(f"\nAll downloads completed! Check the '{output_dir}' folder.")
