import concurrent.futures
import time
import random

def task(name):
    # print(f"Task started by {threading.current_thread().name}")
    print(f"Task {name} starting")
    sleep_time = random.randint(1, 5)
    time.sleep(sleep_time)
    print(f"Task {name} completed after {sleep_time} seconds")
    return sleep_time


# task()

with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:
    # futures = [executor.submit(task) for _ in range(5)]
    # for future in concurrent.futures.as_completed(futures):
    #     result = future.result()
    #     print(f"Task completed with result: {result}")
    
    # results = executor.map(task, range(5))
    # for result in results:
    #     print(f"Task completed with result: {result}")  

    # future_to_task = {executor.submit(task): i for i in range(5)}
    # for future in concurrent.futures.as_completed(future_to_task):
    #     task_id = future_to_task[future]
    #     try:
    #         result = future.result()
    #         print(f"Task {task_id} completed with result: {result}")
    #     except Exception as e:
    #         print(f"Task {task_id} generated an exception: {e}")

    future_to_task = {executor.submit(task, i): i for i in range(5)}
    # for i, m in future_to_task.items():
    #     print(f"Task {i} completed with result: {m}")
    # print(future_to_task.keys())
    # for future in concurrent.futures.as_completed(future_to_task):
    #     task_name = future_to_task[future]
    #     try:
    #         result = future.result()

    for future in concurrent.futures.as_completed(future_to_task):
        task_name = future_to_task[future]
        try:
            result = future.result()
            print(f"Task {task_name} successfully completed with reult: {result}")

        except Exception as e:
            print(f"task {task_name} generated an error {e}")           