from re import L
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@timer
@logger
def slow_add(a, b):
    time.sleep(2)
    return a + b

# print(slow_add(1, 2))

def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    print(f"Calculating fibonacci({n})")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(15))
print(fibonacci(14))
print(fibonacci(16))
print(fibonacci(25))
print(fibonacci(30))
print(fibonacci(35))
print(fibonacci(40))
print(fibonacci(45))
print(fibonacci(50))
print(fibonacci(55))
print(fibonacci(60))
print(fibonacci(65))
print(fibonacci(70))
print(fibonacci(75))