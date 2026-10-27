import time
import psutil
import multiprocessing

head = 101000000
legs = 1000000 * 2 + 100000000 * 4

def find_solution(start_r, end_r, head, legs, result_queue):
    for r in range(start_r, end_r):
        c = head - r
        legs_now = 4 * r + 2 * c
        if legs_now == legs:
            result_queue.put((r, c))
            return

if __name__ == "__main__":
    start = time.time()
    print(f"Start time: {start}")
    num_processes = 100
    chunk = head // num_processes
    processes = []
    result_queue = multiprocessing.Queue()

    for i in range(num_processes):
        start_r = i * chunk + 1
        end_r = (i + 1) * chunk + 1 if i < num_processes - 1 else head
        p = multiprocessing.Process(target=find_solution, args=(start_r, end_r, head, legs, result_queue))
        processes.append(p)
        p.start()

    found = False
    while not found:
        try:
            r, c = result_queue.get(timeout=0.1)
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Solution found: Rabbits: {r}, Chickens: {c}")
            found = True
        except:
            if not any(p.is_alive() for p in processes):
                break

    for p in processes:
        p.terminate()
        p.join()

    end = time.time()
    print(f"End time: {end}")
    print(f"Time taken: {end - start} seconds")
