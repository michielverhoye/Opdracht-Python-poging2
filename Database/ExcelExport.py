# ExcelExport.py
import pandas as pd
from Database.AutoCommands import AutoCommands
from Database.DynoSheetCommands import DynoSheetCommands

class ExcelExport:
    def export_auto_table_to_excel(self):
        auto_commands = AutoCommands()

        autos = auto_commands.get_all_cars()

        if autos:
            auto_df = pd.DataFrame(autos, columns=["Auto_Id", "Merk", "Model", "Kilometers", "ProdYear", "DynoSheet_Id"])

            auto_df.to_excel('auto_data.xlsx', index=False)

            print("Auto table data exported to auto_data.xlsx")
        else:
            print("No data in auto table to export.")

    def export_dyno_table_to_excel(self):
        auto_commands = AutoCommands()
        dyno_commands = DynoSheetCommands(auto_commands)

        dyno_sheets = dyno_commands.view_all_dyno_sheets()

        if dyno_sheets:
            dyno_df = pd.DataFrame(dyno_sheets, columns=["DynoSheet_Id", "MaxHp", "MaxTorque", "Gear", "Fuel", "Auto_Id"])

            dyno_df.to_excel('dyno_data.xlsx', index=False)

            print("Dyno table data exported to dyno_data.xlsx")
        else:
            print("No data in dyno table to export.")
