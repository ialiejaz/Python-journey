def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        print(type(kwargs))

print_kwargs(name = "hello", value = "world!",power = "metal_bending")
