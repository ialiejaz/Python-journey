import time

attempts = 0
max_attempts = 5
wait_time = 1

while attempts < max_attempts:
     print(f"Attempt {attempts + 1} wait time: {wait_time} seconds")
     time.sleep(wait_time)
     wait_time *= 2
     attempts += 1