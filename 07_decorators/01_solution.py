import time

def clock(func):
    def tester(*args,**kwargs):
        start = time.time()
        checker = func(*args,**kwargs)
        end = time.time()
        print(f"The program {func.__name__} ran for {end - start} time")
        return checker
    return tester
@clock
def timer(n):
    time.sleep(n)
   

timer(5)