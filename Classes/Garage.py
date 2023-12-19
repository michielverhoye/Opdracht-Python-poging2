# Classes/garage.py
from Database.AutoCommands import AutoCommands
from Database.DynoSheetCommands import DynoSheetCommands
from Database.CSVExport import CsvExport
from Database.ExcelExport import ExcelExport

class Garage:
    def __init__(self):
        self.auto_commands = AutoCommands()
        self.dynoSheet_commands = DynoSheetCommands(self.auto_commands)
        self.csv_export = CsvExport()
        self.excel_export = ExcelExport()

    def view_all_cars(self):
        all_cars = self.auto_commands.get_all_cars()
        print("All Cars:")
        for car in all_cars:
            print(car)

    def view_all_dynoSheets(self):
        all_dynoSheets = self.dynoSheet_commands.view_all_dyno_sheets()
        print("All Dyno Sheets:")
        print("Id | Hp | Lbs | Gear | Fuel | Car")
        if not all_dynoSheets:
            print("No dyno sheets available.")
        else:
            for dynoSheet in all_dynoSheets:
                print(dynoSheet)

    def park_car(self, merk, model, kilometers, prod_year, dyno_sheet_id=None):
        self.auto_commands.add_car(merk, model, kilometers, prod_year, dyno_sheet_id)

    def remove_car(self, car_id):
        self.auto_commands.remove_car(car_id)

    def drive_car(self, car_id, additional_kilometers):
        self.auto_commands.add_kilometers(car_id, additional_kilometers)

    def create_dyno_sheet(self, auto_id, max_hp, max_torque, gear, fuel):
        self.dynoSheet_commands.create_dyno_sheet(auto_id, max_hp, max_torque, gear, fuel)

    def delete_dyno_sheet(self, dyno_sheet_id):
        self.dynoSheet_commands.delete_dyno_sheet(dyno_sheet_id)
    
    def update_dyno_sheet(self, dyno_sheet_id, max_hp=None, max_torque=None, gear=None, fuel=None):
        self.dynoSheet_commands.update_dyno_sheet(dyno_sheet_id, max_hp, max_torque, gear, fuel)
    
    def get_dyno_sheet_by_id(self, dyno_sheet_id):
        return self.dynoSheet_commands.get_dyno_sheet_by_id(dyno_sheet_id)
    
    def export_auto_table_csv(self):
        self.csv_export.export_auto_table_to_csv()

    def export_dyno_table_csv(self):
        self.csv_export.export_dyno_table_to_csv()

    def export_auto_table_excel(self):
        self.excel_export.export_auto_table_to_excel()

    def export_dyno_table_excel(self):
        self.excel_export.export_dyno_table_to_excel()