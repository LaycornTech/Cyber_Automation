import threading
import time


def print_num():
    for i in range(1, 6):
        print(f"number -- {i}")
        time.sleep(1)

def print_leta():
    for letter in "ABCDE":
        print(f"letter - {letter}") 
        time.sleep(1)


thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_leta)

thread1.start()
thread2.start()

thread1.join()
thread2.join()