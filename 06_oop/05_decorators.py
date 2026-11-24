class Dog:

    def __init__(self,name,color):
            self.__name = name
            self.__color = color
         
    @property
    def color(self):
         return self.__color
    
    # @color.setter
    # def color(self, new_color):
    #     if isinstance(new_color,str) and len(new_color) > 0:
    #         self.__color = new_color
    #     else:
    #         print("Invalid input!")
    
    def bark(self):
            print(f"{self.__name()} says woof! woof!")


dog = Dog("husky","white")
print(dog.color)









