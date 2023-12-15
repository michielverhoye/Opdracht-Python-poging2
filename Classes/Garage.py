# Classes/garage.py
from Database.AutoCommands import AutoCommands
from Database.DinoSheetCommands import DinoSheetCommands

class Garage:
    def __init__(self):
        self.auto_commands = AutoCommands()
        self.dynoSheet_commands = DinoSheetCommands()

    def view_all_cars(self):
        all_cars = self.auto_commands.get_all_cars()
        print("All Cars:")
        for car in all_cars:
            print(car)

    def view_all_dinoSheets(self):
        all_dinoSheets = self.dynoSheet_commands.view_all_dyno_sheets()
        print("All Dino Sheets:")
        for dinoSheet in all_dinoSheets:
            print(dinoSheet)

    def park_car(self, merk, model, kilometers, prod_year, dyno_sheet_id=None):
        self.auto_commands.add_car(merk, model, kilometers, prod_year, dyno_sheet_id)

    def remove_car(self, car_id):
        self.auto_commands.remove_car(car_id)

    def drive_car(self, car_id, additional_kilometers):
        self.auto_commands.add_kilometers(car_id, additional_kilometers)

    def create_dyno_sheet(self, auto_id, max_hp, max_torque, gear, fuel):
        self.dyno_commands.create_dyno_sheet(auto_id, max_hp, max_torque, gear, fuel)
    
    def update_dyno_sheet(self, dyno_sheet_id, max_hp=None, max_torque=None, gear=None, fuel=None):
        self.dyno_commands.update_dyno_sheet(dyno_sheet_id, max_hp, max_torque, gear, fuel)
    
    def get_dyno_sheet_by_id(self, dyno_sheet_id):
        return self.dyno_commands.get_dyno_sheet_by_id(dyno_sheet_id)