class Animals:
    def __init__(self,name,age):
        self.name= name
        self.age = age
        self.health_lvl = 100
        self.happy_lvl = 50
        
    def display_info(self):
        print("-"*30,"Animal Info","-"*30)
        print(f"Name: {self.name}\nAge: {self.age}\nHealth Level: {self.health_lvl}\nHappy Level: {self.happy_lvl}")

        return self
    
    def feed_animal(self):
        self.health_lvl += 10
        self.happy_lvl += 10
        return self
    

class Lions(Animals):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.health_lvl = 150
        self.happy_lvl = 20
        self.mane_length = 30

    def feed_animal(self):
        self.happy_lvl += 25
        self.health_lvl += 35

    def display_info(self):
        super().display_info()
        print(f"Unique Attribute: -> Mane Length: {self.mane_length}")


class Tiger(Animals):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health_lvl = 120
        self.happy_lvl = 15
        self.stripe_count = 40

    def feed_animal(self):
        self.happy_lvl += 20
        self.health_lvl += 30

    def display_info(self):
        super().display_info()
        print(f"Unique Attribute: -> Stripe count: {self.stripe_count}")


class Giraffe(Animals):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health_lvl = 100
        self.happy_lvl = 25
        self.neck_length = 250

    def feed_animal(self):
        self.happy_lvl += 15
        self.health_lvl += 20

    def display_info(self):
        super().display_info()
        print(f"Unique Attribute: -> Neck Length: {self.neck_length}")


giraffe1 = Giraffe("gi1",22)
tiger1 = Tiger("tig1", 2)

giraffe1.feed_animal()
giraffe1.display_info()
