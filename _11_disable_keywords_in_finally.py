def my_method():
    try:
        # raise ValueError()
        return "try"
    except ValueError:
        return "except"
    finally:
        return "finally"


print(my_method())
