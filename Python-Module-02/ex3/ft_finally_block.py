#! /usr/bin/env python3

def water_plants(plant_list: list) -> None:
    print("Opening watering system")

    try:
        for plant in plant_list:
            if not plant:
                raise ValueError
            print(f"Watering {plant}")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!\n")

    plant_list = ["tomato", None, "carrots"]
    print("Testing with error..")
    water_plants(plant_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    try:
        test_watering_system()
    except Exception as e:
        print(e)
