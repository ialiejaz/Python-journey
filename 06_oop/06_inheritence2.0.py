class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class kingdom:
    def animalia(self):
        return "animal"

class phylum:
    def animal(self):
        return "sapiens"

class species:
    def species(self):
        return "homo"

class humans(kingdom,phylum,species):
    pass

human1 = humans()
print(human1.animalia())
print(human1.animal())
print(human1.species())