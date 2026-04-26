#! /usr/bin/env python3

class GardenError(Exception):
    def __init__(self: object, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self: object, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self: object, message: str) -> None:
        super().__init__(message)


class GardenManager():
    def __init__(self: object, water_tank: int) -> None:
        self.plants = {}
        self.water_tank = 0
        system_recovered = False
        try:
            if water_tank <= 0:
                system_recovered = True
                raise GardenError("Caught GardenError: "
                                  "Not enough water in tank")
            self.water_tank = water_tank
        except GardenError as e:
            print(e)
        finally:
            if system_recovered:
                print("System recovered and continuing...\n")

    def add_plant(self: object, name: str, water: int, sun: int) -> None:
        try:
            if not name:
                raise PlantError("Error adding plant: "
                                 "Plant name cannot be empty!\n")
            self.plants[name] = {"water": water, "sun": sun}
            print(f"Added {name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(self: object) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants.keys():
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self: object) -> None:
        try:
            for plant in self.plants.keys():
                if not 1 <= self.plants[plant]["water"] <= 10:
                    raise WaterError(f"Error checking {plant}: Water level "
                                     f"{self.plants[plant]['water']} is "
                                     "too high (max 10)\n")
                print(f"{plant}: healthy (water: {self.plants[plant]['water']}"
                      f", sun: {self.plants[plant]['sun']})")
        except WaterError as e:
            print(e)


def test_garden_management() -> None:
    garden1 = GardenManager(30)
    print("Adding plants to garden...")
    garden1.add_plant("tomato", 5, 8)
    garden1.add_plant("lettuce", 15, 7)
    garden1.add_plant("", 12, 9)

    print("Watering plants...")
    garden1.water_plants()

    print("Checking plant health...")
    garden1.check_plant_health()

    print("Testing error recovery..")
    GardenManager(0)

    print("Garden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")

    try:
        test_garden_management()
    except Exception as e:
        print(e)
