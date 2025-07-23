import os
import time

print(os.getpid())
counter = 1
while True:
    counter += 1
    time.sleep(1)
