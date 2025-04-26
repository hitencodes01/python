# Make a decorator repeat_decorator that repeats the function output n times.

def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            result = func()
            return 3*result
        return wrapper
    return decorator
@repeat_decorator(n=3)
def greet():
    return "Hi! "
print(greet())