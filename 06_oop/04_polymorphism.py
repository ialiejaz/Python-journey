class SUV:

    total_cars = 0
    
    def __init__(self,brand,model,fuel):
        self.brand = brand
        self.model = model
        self.__fuel = fuel
        SUV.total_cars += 1

    def get_fuel(self): 
        return self.__fuel
    def set_fuel(self,new_fuel):
        if (new_fuel) != "petrol":
            self.__fuel = new_fuel
        else:
            print("wromg fuel type selected!")

    def color(self):
            return "White pearl"

class sedan(SUV):

    def __init__(self,brand,model,capacity,fuel):
        super().__init__(brand,model,fuel)
        self.capacity = capacity

    # def fuel_type(self):
    #     return "PetrOl".lower()
    def color(self):
        return "Black pearl"


my_SUV = SUV("Toyota","Land Cruiser","Diesel")
my_sedan = sedan("Toyota","Corolla","7","")
my_sedan.set_fuel("pEtrol")

print(f"The {my_SUV.brand} {my_SUV.model} 300 has a twin turbo  {my_SUV.get_fuel().lower()} engine. I like the {my_SUV.color()} one.")
print(f"The {my_sedan.brand} {my_sedan.model} 1.8 has a Dual vvti  {my_sedan.get_fuel()} engine. My favourite is the one in {my_SUV.color()} color.")
print(SUV.total_cars)