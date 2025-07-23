# Python 3 pre 3.14:
try:
    raise ValueError("An error occurred")
except (TimeoutError, ValueError):
    print("Something went wrong! Or did it?")

# Python 3.14+:
try:
    raise ValueError("An error occurred")
except TimeoutError, ValueError:
    print("Something went wrong! Or did it?")


# python3.14 _07_exception_parantheses.py
