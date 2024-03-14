class vehicles():
    def __init__(self, make, model, year):
        self.type = 'generic vehicle'
        self.make = make
        self.model = model
        self.year = year

    def honk(self):
        return self.sound
    
    @property
    def howManyWheels(self):
        return self.wheels

class Car(vehicles):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year)
        self.color = color
        self.sound = sound
        self.wheels = 4


class Motorcycle(vehicles):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year)
        self.color = color
        self.sound = sound
        self.wheels = 2
    
   
    