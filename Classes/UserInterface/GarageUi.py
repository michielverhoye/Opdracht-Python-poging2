# Classes/userinterface/GarageUi.py
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
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.view_all_cars()
            elif choice == "2":
                self.park_car()
            elif choice == "3":
                self.drive_car()
            elif choice == "4":
                self.remove_car()
            elif choice == "5":
                print("Exiting the Garage Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

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


if __name__ == "__main__":
    ui = GarageUI()
    ui.run()
