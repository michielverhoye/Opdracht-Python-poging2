# CSVExport.py
import pandas as pd
from Database.AutoCommands import AutoCommands
from Database.DynoSheetCommands import DynoSheetCommands

class CsvExport:
    def export_auto_table_to_csv(self):
        auto_commands = AutoCommands()

        autos = auto_commands.get_all_cars()

        if autos:
            auto_df = pd.DataFrame(autos, columns=["Auto_Id", "Merk", "Model", "Kilometers", "ProdYear", "DynoSheet_Id"])

            # Export to CSV
            auto_df.to_csv('auto_data.csv', index=False)

            print("Auto table data exported to auto_data.csv")
        else:
            print("No data in auto table to export.")

    def export_dyno_table_to_csv(self):
        auto_commands = AutoCommands()
        dyno_commands = DynoSheetCommands(auto_commands)

        dyno_sheets = dyno_commands.view_all_dyno_sheets()

        if dyno_sheets:
            dyno_df = pd.DataFrame(dyno_sheets, columns=["DynoSheet_Id", "MaxHp", "MaxTorque", "Gear", "Fuel", "Auto_Id"])

            # Export to CSV
            dyno_df.to_csv('dyno_data.csv', index=False)

            print("Dyno table data exported to dyno_data.csv")
        else:
            print("No data in dyno table to export.")
