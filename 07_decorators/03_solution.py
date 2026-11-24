import time

def cache(func):

    cache_value  = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper




@cache
def sum_function(a, b):
    time.sleep(3)
    return a + b

print(sum_function(10, 20))
print(sum_function(10, 20))
print(sum_function(10, 10))