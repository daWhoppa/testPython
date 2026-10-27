import time
import psutil

head = 101000000
legs = 1000000 * 2 + 100000000 * 4

rabbit = (legs - 2 * head) / 2
chicken = head - rabbit

start = time.time()
print(str(start))
for r in range(1, int(head)):
    c = head - r
    legs_now = 4 * r + 2 * c
    if(legs_now == legs):
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Solution found: Rabbits: {r}, Chickens: {c}")
        break
end = time.time()
print(str(end)) 
print(f"Time taken: {end - start} seconds")
