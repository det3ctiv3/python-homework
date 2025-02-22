def check(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print("Denominator can't be zero")
            return None

        return func(*args, **kwargs)

    return wrapper

@check
def div(a, b):
    return a / b

print(div(10, 0))
print(div(10, 5))
print(div(0, 0))