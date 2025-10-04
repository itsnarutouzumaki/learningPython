import time

wait_time = 1  # initial wait time in seconds
max_try=5  # maximum number of retries
try_count = 0

while try_count < max_try:
  try_count+=1
  print(f"Attempt {try_count} waiting for {wait_time} seconds...")
  time.sleep(wait_time)
  wait_time *= 2 # double the wait time for next attempt

print("Max attempts reached. Exiting...")