import time

counter = 1
while True:
    counter += 1
    time.sleep(1)

# python3.14 _04_remote_debugging.py &
# python3.14 -m pdb -p PID
# docker run -it --rm -v $(pwd):/data  python:3.14-rc-bookworm bash
