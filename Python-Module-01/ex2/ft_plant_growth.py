#! /usr/bin/env python3

class Plant:
    """Class for plants object"""
    def __init__(self: object, name: str, height: int, ages: int) -> None:
        """plants information"""
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self: object) -> None:
        """increment height by 1"""
        self.height += 1

    def age(self: object) -> None:
        """increment ages by 1 and call grow"""
        self.ages += 1
        self.grow()

    def get_info(self: object) -> None:
        """Display plants information"""
        print(f"{self.name}: {self.height}cm, {self.ages} days old")


if __name__ == "__main__":
    y = 0
    i = 0
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Soso", 27, 14)
    plants_list = [plant1]
    old_height = [plant1.height]

    print("=== Day 1 ===")
    for plant in plants_list:
        plant.get_info()

    for plant in plants_list:
        for day in range(6):
            plant.age()
    new_height = [plant1.height]

    print("=== Day 7 ===")
    for plant in plants_list:
        plant.get_info()
        print(f"Growth this week: +{new_height[y] - old_height[i]}cm")
        y += 1
        i += 1
