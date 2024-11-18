
import time
current_time = time.time()
print(current_time)

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{function.__name__} run speed: {run_time}s")
        return result
    return wrapper
    
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
    
fast_function()
slow_function()
