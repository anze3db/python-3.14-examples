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

# Python 2:
try:
    raise ValueError()
except ValueError, e:
    print("Caught a ValueError:", e)
