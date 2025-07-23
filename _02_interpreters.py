import os
from concurrent.futures import (
    InterpreterPoolExecutor,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
)

# With multiple isolated interpreters, you can take advantage of a class of concurrency models, like CSP or the actor model, that have found success in other programming languages, like Smalltalk, Erlang, Haskell, and Go. Think of multiple interpreters like threads but with opt-in sharing.

# 3.12 where interpreters were finally properly isolated and stopped sharing the GIL.


def fib_task(n: int) -> int:
    if n <= 1:
        return n
    return fib_task(n - 1) + fib_task(n - 2)


tasks = os.cpu_count() or 2


def run_fib_int():
    with InterpreterPoolExecutor(max_workers=tasks) as executor:
        for _ in range(tasks):
            executor.submit(fib_task, 35)


def run_fib_proc():
    with ProcessPoolExecutor(max_workers=tasks) as executor:
        for _ in range(tasks):
            executor.submit(fib_task, 35)


# python3.14 -m timeit -n 1 -r 1 -s 'import _02_interpreters' '_02_interpreters.run_fib_int()'
# python3.14 -m timeit -n 1 -r 1 -s 'import _02_interpreters' '_02_interpreters.run_fib_proc()'
