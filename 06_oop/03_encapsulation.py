class Animal:

    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self,new_name):
         if len(new_name) > 0:
              self.__name = new_name
         else:
              print("name cannot be empty!")

    def eat(self):
        print(f"{self.get_name()} is eating.")

class Dog(Animal):
    
    def __init__(self,name):
         super().__init__(name)
        
    def bark(self):
            print(f"{self.get_name()} says woof! woof!")


my_dog = Dog('shephered')
my_dog2 = Dog('german_shephered')
my_dog.set_name("Siberian_husky")

# print(my_dog.name)
print(my_dog.get_name())

my_dog.eat()
my_dog.bark()