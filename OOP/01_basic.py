# class Car:
#     make = ""
#     model = ""

# my_car = Car()
# my_car.make = "Toyota"
# my_car.model = "MK5"

# old_car = Car()

# old_car.make = "Toyota"
# old_car.model = "88 Model"

# print(f"My daily use car is a {old_car.make} {old_car.model}.")
# print(f"But I also have a {my_car.model}.")

class Bike:
    def __init__(self,make,model):

        self.make = make
        self.model = model

    def full_name(self):
        return f"{self.make} {self.model}"

old_bike = Bike("Yamaha","YB100")
my_bike = Bike('Honda','cbx')
# print(my_bike.full_name())


# print(f"My daily use bike is a {my_bike.make} {my_bike.model}.")
# print(f"But I also have a {old_bike.make} {old_bike.model}.")
        
class Ev(Bike):

    def __init__(self,make,model,battery):
        super().__init__(make,model)
        self.battery = battery

my_ebike = Ev("United","Bullet","800Kw")
print(f"I have a {my_ebike.make} {my_ebike.model} and it has a powerfull {my_ebike.battery} in it.")