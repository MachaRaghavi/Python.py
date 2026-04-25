import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()       
        result = func(*args, **kwargs)        
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

example_function()
