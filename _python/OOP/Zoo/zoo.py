from animals import *

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.animals_types = {"lion": lambda name,age: self.animals.append(Lions(name,age)), 
                            "tiger": lambda name,age: self.animals.append(Tiger(name,age)),
                            "giraffe": lambda name,age: self.animals.append(Giraffe(name,age))}

    def add_animal(self,animal_type, animal_name, animal_age):
        self.animals_types[animal_type](animal_name,animal_age)
        return self
    
    def print_all_info(self):
        print("-"*30,self.name,"-"*30)
        for animal in self.animals:
            animal.display_info()



# Creating a zoo instance
zoo = Zoo("My Zoo")

# Adding animals to the zoo
zoo.add_animal("lion", "Simba", 5)
zoo.add_animal("tiger", "Shere Khan", 6)
zoo.add_animal("giraffe", "Melman", 8)

# Printing all information about the animals in the zoo
zoo.print_all_info()
