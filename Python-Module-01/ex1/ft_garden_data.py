#! /usr/bin/env python3

class Plant:
    """Class for plants object"""
    def __init__(self: object, name: str, height: int, age: int) -> None:
        """plants information"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant_list = [plant1, plant2, plant3]
    for i in range(3):
        print(plant_list[i].name + ":", end=" ")
        print(f"{plant_list[i].height}cm,", end=" ")
        print(f"{plant_list[i].age} days old")
