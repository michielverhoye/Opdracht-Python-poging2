# Classes/garage.py
from Database.AutoCommands import AutoCommands

class Garage:
    def __init__(self):
        self.auto_commands = AutoCommands()

    def view_all_cars(self):
        all_cars = self.auto_commands.get_all_cars()
        print("All Cars:")
        for car in all_cars:
            print(car)

    def park_car(self, merk, model, kilometers, prod_year, dyno_sheet_id=None):
        self.auto_commands.add_car(merk, model, kilometers, prod_year, dyno_sheet_id)

    def remove_car(self, car_id):
        self.auto_commands.remove_car(car_id)

    def drive_car(self, car_id, additional_kilometers):
        self.auto_commands.add_kilometers(car_id, additional_kilometers)
