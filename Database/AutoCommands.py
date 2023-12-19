import sqlite3

class AutoCommands:
    def __init__(self, database_name='Database/GarageDb.db'):
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def get_all_cars(self):
        query = 'SELECT * FROM "Auto"'
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def get_car_by_id(self, car_id):
        query = 'SELECT * FROM "Auto" WHERE "Id" = ?'
        self.cursor.execute(query, (car_id,))
        car = self.cursor.fetchone()
        return car

    def add_car(self, merk, model, kilometers, prod_year, dyno_sheet_id=None):
        query = 'INSERT INTO "Auto" ("Merk", "Model", "Kilometers", "ProdYear", "DynoSheetId") VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(query, (merk, model, kilometers, prod_year, dyno_sheet_id))
        self.conn.commit()

    def remove_car(self, car_id):
        query = 'DELETE FROM "Auto" WHERE "Id" = ?'
        self.cursor.execute(query, (car_id,))
        self.conn.commit()

    def add_kilometers(self, car_id, additional_kilometers):
        query = 'UPDATE "Auto" SET "Kilometers" = "Kilometers" + ? WHERE "Id" = ?'
        self.cursor.execute(query, (additional_kilometers, car_id))
        self.conn.commit()
