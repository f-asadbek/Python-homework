a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

def check(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@check
def div(a, b):
    return a / b
try:
    print(div(a, b))
except ZeroDivisionError:
    print("Denominator can't be zero")