class Car:
    def __init__(self, brand, model, year, road):
        self.brand = brand
        self.model = model
        self.year = year
        self.road = road

    def info(self):
        return f"{self.brand}, {self.model}, {self.year} год, {self.road} км"
