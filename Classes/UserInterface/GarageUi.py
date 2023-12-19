from Classes.Garage import Garage

class GarageUI:
    def __init__(self):
        self.garage = Garage()

    def display_menu(self):
        print("\nGarage Management System")
        print("1. View All Cars")
        print("2. Park Car")
        print("3. Drive Car")
        print("4. Remove Car")
        print("5. Open Dyno Sheet menu")
        print("6. Open Export menu")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.view_all_cars()
            elif choice == "2":
                self.park_car()
            elif choice == "3":
                self.drive_car()
            elif choice == "4":
                self.remove_car()
            elif choice == "5":
                self.dyno_sheet_menu()
            elif choice == "6":
                self.export_menu()
            elif choice == "7":
                print("Exiting the Garage Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def dyno_sheet_menu(self):
        while True:
            print("\nDyno Sheet Menu:")
            print("1. Create Dyno Sheet")
            print("2. Update Dyno Sheet")
            print("3. View All Dyno Sheets")
            print("4. Delete Dyno Sheet")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_dyno_sheet()
            elif choice == '2':
                self.update_dyno_sheet()
            elif choice == '3':
                self.view_all_dyno_sheets()
            elif choice == '4':
                self.delete_dyno_sheet()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def export_menu(self):
        while True:
            print("\nExport Menu:")
            print("1. Export cars to CSV")
            print("2. Export cars to Excel")
            print("3. Export dyno sheets to CSV")
            print("4. Export dyno sheets to Excel")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.export_autotable_to_csv()
            elif choice == '2':
                self.export_autotable_to_excel()
            elif choice == '3':
                self.export_dynotable_to_csv()
            elif choice == '4':
                self.export_dynotable_to_excel()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_all_cars(self):
        cars = self.garage.view_all_cars()

        if cars is None:
            print("Error fetching cars. Please check the database connection.")
        elif len(cars) == 0:
            print("No cars in the garage.")
        else:
            for car in cars:
                print(car)

    def park_car(self):
        merk = input("Enter the car's brand: ")
        model = input("Enter the car's model: ")
        kilometers = int(input("Enter the current kilometers: "))
        prod_year = int(input("Enter the production year: "))
        dyno_sheet_id_input = input("Enter the DynoSheetId (press Enter if none): ")

        if dyno_sheet_id_input.strip():  # Check if the input is not an empty string
            dyno_sheet_id = int(dyno_sheet_id_input)
        else:
            dyno_sheet_id = None

        self.garage.park_car(merk, model, kilometers, prod_year, dyno_sheet_id)
        print("Car parked successfully.")

    def drive_car(self):
        car_id = int(input("Enter the car ID to drive: "))
        additional_kilometers = int(input("Enter the additional kilometers to drive: "))

        self.garage.drive_car(car_id, additional_kilometers)
        print("Car driven successfully.")

    def remove_car(self):
        car_id = int(input("Enter the car ID to remove: "))
        self.garage.remove_car(car_id)
        print("Car removed successfully.")

    def create_dyno_sheet(self):
        auto_id = int(input("Enter the AutoId for the car: "))
        max_hp = float(input("Enter the Max HP: "))
        max_torque = float(input("Enter the Max Torque: "))
        gear = int(input("Enter the Gear: "))
        fuel = input("Enter the Fuel type: ")

        self.garage.create_dyno_sheet(auto_id, max_hp, max_torque, gear, fuel)

    def update_dyno_sheet(self):
        dyno_sheet_id = int(input("Enter the DynoSheetId to update: "))
        max_hp = float(input("Enter the new Max HP (press Enter to skip): "))
        max_torque = float(input("Enter the new Max Torque (press Enter to skip): "))
        gear = int(input("Enter the new Gear (press Enter to skip): "))
        fuel = input("Enter the new Fuel type (press Enter to skip): ")

        self.garage.update_dyno_sheet(dyno_sheet_id, max_hp, max_torque, gear, fuel)

    def view_all_dyno_sheets(self):
        self.garage.view_all_dynoSheets()

    def delete_dyno_sheet(self):
        dyno_sheet_id = int(input("Enter the dyno sheet Id: "))
        self.garage.delete_dyno_sheet(dyno_sheet_id)

    def export_autotable_to_csv(self):
        self.garage.export_auto_table_csv()

    def export_dynotable_to_csv(self):
        self.garage.export_dyno_table_csv()

    def export_autotable_to_excel(self):
        self.garage.export_auto_table_excel()
    
    def export_dynotable_to_excel(self):
        self.garage.export_dyno_table_excel()

if __name__ == "__main__":
    ui = GarageUI()
    ui.run()
