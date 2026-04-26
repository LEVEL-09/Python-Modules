#! /usr/bin/env python3

class Plant:
    """Class for plants object"""
    def __init__(self: object, name: str, height: int, age: int) -> None:
        """plants information"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self: object, name: str, height: int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self: object) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self: object, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self: object) -> None:
        result = (2*3.14*(self.trunk_diameter/2)*self.height) / 1000
        print(f"{self.name} provides {result:.0f} "
              f"square meters of shade")


class Vegetable(Plant):
    def __init__(self: object, name: str, height: int, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self: object) -> None:
        print(f"{self.name} is rich in vitamin C")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Zinnia", 22, 12, "pink")
    print(f"{flower1.name} (Flower): {flower1.height}cm, {flower1.age} days, "
          f"{flower1.color} color")
    flower1.bloom()

    print("")

    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Pine", 511, 34567, 70)
    print(f"{tree1.name} (Tree): {tree1.height}cm, {tree1.age} days, "
          f"{tree1.trunk_diameter} diameter")
    tree1.produce_shade()

    print("")

    vegetable1 = Vegetable("Tomato", 80, 90, "summer")
    vegetable2 = Vegetable("Parsnips", 2, 130, "winter")
    print(f"{vegetable1.name} (Vegetable): {vegetable1.height}cm, "
          f"{vegetable1.age} days, {vegetable1.harvest_season} harvest")
    vegetable1.nutritional_value()
