from tqdm import tqdm
import time
import os
import subprocess

# Calls the Windows host shutdown utility directly from WSL
# def shutdown_windows_from_wsl():
#     try:
#         # Calls the Windows side shutdown utility directly across the WSL interoperability bridge
#         subprocess.run(["shutdown.exe", "/s", "/t", "30"], check=True)
#     except subprocess.CalledProcessError:
#         print("Could not trigger Windows host shutdown. Ensure interop is enabled.")

# shutdown_windows_from_wsl()

# for i in tqdm.tqdm(range(100), desc="Processing"):
#     time.sleep(0.1)

def simulate_work(item):
    time.sleep(5)  # Simulate some work being done

for item in tqdm(range(10), desc="Simulating Work"):
    simulate_work(item)


