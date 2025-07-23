def my_method():
    try:
        # raise ValueError()
        return "try"
    except ValueError:
        # raise ValueError()
        return "except"
    finally:
        return "finally"


print(my_method())

# python3.14 _11_disable_keywords_in_finally.py
