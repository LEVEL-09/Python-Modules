#! /usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    is_healthy = True
    try:
        if not plant_name:
            is_healthy = False
            raise ValueError
    except ValueError:
        print("Error: Plant name cannot be empty!\n")
    try:
        if not 1 <= water_level <= 10:
            is_healthy = False
            raise ValueError
    except ValueError:
        if water_level > 10:
            print(f"Error: Water level {water_level} is too high (max 10)\n")
        else:
            print(f"Error: Water level {water_level} is too low (min 1)\n")
    try:
        if not 2 <= sunlight_hours <= 12:
            is_healthy = False
            raise ValueError
    except ValueError:
        if sunlight_hours < 2:
            print(f"Error: Sunlight hours {sunlight_hours} is "
                  "too low (min 2)\n")
        else:
            print(f"Error: Sunlight hours {sunlight_hours} is "
                  "too high (max 12)\n")
    if is_healthy:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 11)
    except Exception as e:
        print(e)

    print("Testing empty plant name...")
    try:
        check_plant_health("", 6, 12)
    except Exception as e:
        print(e)

    print("Testing bad water level...")
    try:
        check_plant_health("carrot", 15, 10)
    except Exception as e:
        print(e)

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("potatoes", 7, 0)
    except Exception as e:
        print(e)

    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")

    try:
        test_plant_checks()
    except Exception as e:
        print(e)
