import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(end - start)
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(5)
    print("Done")

slow_function()