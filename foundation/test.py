
import concurrent.futures, threading
import time
# dim = {"name": "mike", "age": 20, "city": "New York"}

# dim[me] = dom["name"], dim["age"], dim["city"]

# print(dim["name"])
# for me in dim.keys():
#     print(dim[me])


list1 = [1, 2, 3, 4, 5]
def print_list():
    for i in range(len(list1)):
        print(f"number -- {list1[i]}")
        time.sleep(1)
list2 = ["Abbey", "Bola", "Cabdy", "Disi", "Ema"]
def print_leta():
    for word in list2:
        print(f"letter - {word}") 
        time.sleep(1)

# print_leta(), 
# print_list()

# thread1 = threading.Thread(target = print_list)
# thread2 = threading.Thread(target = print_leta)

# thread1.start()
# thread2.start()

with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:
    future_task = {executor.submit(print_list): i for i in range(5)}

    for future in concurrent.futures.as_completed(future_task):
        task_named = future_task[future]
        print(f"Task completed: {task_named}")
    # print(future_to_task.keys()) ===> prints output thrice then twice
    # executor.submit(print_list)
    # executor.submit(print_leta)
