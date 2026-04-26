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


def raise_error(input: int) -> None:
    try:
        if input < 10:
            raise PlantError("Caught PlantError: The tomato plant is wilting!")
        elif input < 20:
            raise WaterError("Caught WaterError: Not enough water in the "
                             "tank!")
        elif input < 25:
            raise GardenError("Caught a garden error: The tomato plant is "
                              "wilting!")
        elif input < 30:
            raise GardenError("Caught a garden error: Not enough water in "
                              "the tank!")
    except (PlantError, WaterError, GardenError) as e:
        print(e)


def main() -> None:
    print("Testing PlantError...")
    raise_error(1)

    print("\nTesting WaterError...")
    raise_error(15)

    print("\nTesting catching all garden errors...")
    raise_error(23)
    raise_error(27)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    try:
        main()
    except Exception as e:
        print(e)
