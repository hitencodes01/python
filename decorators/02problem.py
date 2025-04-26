# Create a decorator called uppercase_decorator that takes a function returning a string and makes the result uppercase.
def uppercase_decorator(func):
    def wrapper(*args):
        result =  func(*args)
        return result.upper()
    return wrapper
@uppercase_decorator
def asWritten(sentence):
    return sentence

print(asWritten("hello"))