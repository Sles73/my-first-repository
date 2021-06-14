class Car: 
    """Jednoduchá pokus o reprezentaci auta"""

    def __init__(self, make, model, year):
        """Inicializuje atributy které popisují auto"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Vrátí hezky zformáované jméno"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_car = Car("BMW","E30","1991")
print(f"{my_car.get_descriptive_name()} is my favorite car.")