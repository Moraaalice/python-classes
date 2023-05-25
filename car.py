class Car:
    wheels = "Four"
    def __init__(self,make,model,year,color,speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
    
    def age_of_car(self):
        return 2023-self.year
    
    def description_of_car(self):
        return f"The car is a {self.make} {self.model} and its {self.color} in color"
    
    def distance_covered(self,time):
        return f"The car covered a distance of {self.speed*time} kms"
 