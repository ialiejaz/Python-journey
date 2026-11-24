def debug(func):
    def wrapper(*args,**kwargs):
        str_arg = ', '.join(str(arg) for arg in args)
        kwags_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling {func.__name__} with args : {args} and kwargs : {kwargs}")
        return func(*args,**kwargs)
    return wrapper

@debug
def greeting(name, greeting):
    print(f"{greeting}, Mr.{name}")

greeting(name = "aslam", greeting = "hello!")