from DZ.cars.car import Car


class Electro(Car):
    def __init__(self, brand, model, year, road, power):
        super().__init__(brand, model, year, road)
        self.power = power

    def info(self):
        return f"{super().info()}\nЭтот автомобиль имеет мощность {self.power} %"
