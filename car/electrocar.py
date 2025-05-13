from car.carclass import CarClass


class ElectroCar(CarClass):
    def __init__(self, brand, model, year, run, batt):
        super().__init__(brand, model, year, run)
        self.batt = batt

    def descrip_battery(self):
        print(f"Этот автомобиль имеет можность {self.batt}")


