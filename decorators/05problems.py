def doubles_decorator(func):
    def wrapper(*args):
        result = 2 * func(*args)
        return result
    return wrapper
def squares_decorator(func):
    def wrapper(*args):
        result = func(*args)**2
        return result
    return wrapper
@squares_decorator
@doubles_decorator
# In Python, the nearest decorator (the one closest to the function) is applied first.
def test(a):
    return a
print(test(2))