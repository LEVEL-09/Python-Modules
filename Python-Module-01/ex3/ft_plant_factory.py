#! /usr/bin/env python3

class Plant:
    """Class for plants object"""

    total = 0

    def __init__(self: object, name: str, height: int, age: int) -> None:
        """plants information"""
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1


def factory(name: str, height: int, age: int) -> object:
    print(f"Created: {name} ({height}cm, {age} days)")
    return Plant(name, height, age)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plant_list = [factory("Rose", 25, 30), factory("Oak", 200, 365),
                  factory("Cactus", 5, 90), factory("Sunflower", 80, 45),
                  factory("Fern", 15, 120)]

    print(f"\nTotal plants created: {Plant.total}")
