import os
from concurrent.futures import ThreadPoolExecutor


def fib_task(n: int) -> int:
    if n <= 1:
        return n
    return fib_task(n - 1) + fib_task(n - 2)


tasks = os.cpu_count() or 2


def run_fib():
    with ThreadPoolExecutor(max_workers=tasks) as executor:
        for _ in range(tasks):
            executor.submit(fib_task, 35)


# python3.14 -m timeit -n 1 -r 1 -s 'import _01_free_threaded' '_01_free_threaded.run_fib()'
