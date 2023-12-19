import sqlite3

class DynoSheetCommands:
    def __init__(self, auto_commands, database_name='Database/GarageDb.db'):
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.auto_commands = auto_commands

    def disconnect(self):
        self.conn.close()

    def create_dyno_sheet(self, auto_id, max_hp, max_torque, gear, fuel):
        auto = self.auto_commands.get_car_by_id(auto_id)
        if not auto:
            print(f"Error: Auto with ID {auto_id} not found.")
            return

        query = """
            INSERT INTO "DynoSheet" ("MaxHp", "MaxTorque", "Gear", "Fuel", "AutoId")
            VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (max_hp, max_torque, gear, fuel, auto_id))
        self.conn.commit()
        print("DynoSheet created successfully.")

    def update_dyno_sheet(self, dyno_sheet_id, max_hp=None, max_torque=None, gear=None, fuel=None):
        dyno_sheet = self.get_dyno_sheet_by_id(dyno_sheet_id)
        if not dyno_sheet:
            print(f"Error: DynoSheet with ID {dyno_sheet_id} not found.")
            return

        update_query = "UPDATE DynoSheet SET "
        update_params = []

        if max_hp is not None:
            update_query += "MaxHp = ?, "
            update_params.append(max_hp)

        if max_torque is not None:
            update_query += "MaxTorque = ?, "
            update_params.append(max_torque)

        if gear is not None:
            update_query += "Gear = ?, "
            update_params.append(gear)

        if fuel is not None:
            update_query += "Fuel = ?, "
            update_params.append(fuel)

        update_query = update_query.rstrip(', ')

        update_query += " WHERE Id = ?"
        update_params.append(dyno_sheet_id)

        self.cursor.execute(update_query, tuple(update_params))
        self.conn.commit()
        print(f"DynoSheet with ID {dyno_sheet_id} updated successfully.")

    def get_dyno_sheet_by_id(self, dyno_sheet_id):
        query = 'SELECT * FROM "DynoSheet" WHERE "Id" = ?'
        self.cursor.execute(query, (dyno_sheet_id,))
        dyno_sheet = self.cursor.fetchone()
        return dyno_sheet

    def view_all_dyno_sheets(self):
        query = 'SELECT * FROM "DynoSheet"'
        self.cursor.execute(query)
        dyno_sheets = self.cursor.fetchall()

        
        return dyno_sheets
        
    def delete_dyno_sheet(self, dyno_sheet_id):
        query = 'DELETE FROM "DynoSheet" WHERE "Id" = ?'
        self.cursor.execute(query, (dyno_sheet_id,))
        self.conn.commit()
