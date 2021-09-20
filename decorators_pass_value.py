
# Decorator with pass value on param
def with_custom_message(message):
    def with_message(function):
        print(f"{message}")
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message

@with_custom_message("holi")
def multiply(a, b):
    c = a * b
    print(f"The result of {a} * {b} = {c}")

multiply(5, 5)