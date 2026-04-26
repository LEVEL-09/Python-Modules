#! /usr/bin/env python3

class GardenManager():
    total_gardens = 0

    def __init__(self: object) -> None:
        self.list = []

    def create_garden_network(self: object) -> None:
        print("Garden scores - ", end="")

        last_garden = None

        for g in self.list:
            last_garden = g

        for i in self.list:
            x = 0
            for y in i.list:
                if y.__class__ is PrizeFlower:
                    x += y.height + (y.prize * 4)
                else:
                    x += y.height
            if i is not last_garden:
                print(f"{i.name}: {x}, ", end="")
            else:
                print(f"{i.name}: {x}", end="")
        print("")

    def validate_height(height: int) -> None:
        if (height > 0):
            print("Height validation test: True")
        else:
            print("Height validation test: False")
    validate_height = staticmethod(validate_height)

    def total_gardens_managed(cls: object) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")
    total_gardens_managed = classmethod(total_gardens_managed)

    def create_garden(cls: object, obj: object, name: str) -> object:
        return cls.Garden(name, obj)
    create_garden = classmethod(create_garden)

    class Garden():
        plants_added = 0
        total_growth = 0

        def __init__(self: object, name: str, manger: object) -> None:
            self.name = name
            self.list = []
            manger.list.append(self)
            GardenManager.total_gardens += 1

        def add_plant(self: object, plant: object) -> None:
            if plant not in self.list:
                print(f"Added {plant.name} to {self.name}'s garden")
                self.list.append(plant)
                GardenManager.Garden.plants_added += 1

        def plants_grow(self: object) -> None:
            print(f"{self.name} is helping all plants grow...")
            for i in self.list:
                i.grow()
                print(f"{i.name} grew 1cm")
                GardenManager.Garden.total_growth += 1

        def plants_type(self: object, garden: object) -> None:
            regular = 0
            flowering = 0
            prize_flowers = 0

            for i in self.list:
                if i.__class__ is Plant:
                    regular += 1
                elif i.__class__ is FloweringPlant:
                    flowering += 1
                elif i.__class__ is PrizeFlower:
                    prize_flowers += 1

            garden.regular = regular
            garden.flowering = flowering
            garden.prize_flowers = prize_flowers

    class GardenStats():
        def __init__(self: object, manager: object) -> None:
            self.manager = manager

        def plants_stats(self: object) -> None:
            print("Plants in garden:")
            for i in self.manager.list:
                if i.__class__ is Plant:
                    print(f"- {i.name}: {i.height}cm")
                elif i.__class__ is FloweringPlant:
                    print(f"- {i.name}: {i.height}cm {i.color} "
                          f"flowers ", end="")
                    if i.blooming is True:
                        print("(blooming)")
                    else:
                        print("(not blooming)")
                elif i.__class__ is PrizeFlower:
                    print(f"- {i.name}: {i.height}cm {i.color} "
                          f"flowers ", end="")
                    if i.blooming is True:
                        print("(blooming)", end="")
                    else:
                        print("(not blooming)", end="")
                    print(f", Prize points: {i.prize}")

        def added_and_growth(self: object) -> None:
            print(f"Plants added: {self.manager.plants_added}, "
                  f"Total growth: {self.manager.total_growth}cm")

        def plants_type(self: object) -> None:
            self.manager.plants_type(self)
            print(f"Plant types: {self.regular} regular, {self.flowering} "
                  f"flowering, {self.prize_flowers} prize flowers")


class Plant():
    def __init__(self: object, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self: object):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self: object, name: str, height: int,
                 color: str, blooming: bool) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self: object, name: str, height: int,
                 color: str, blooming: bool, prize: int) -> None:
        super().__init__(name, height, color, blooming)
        self.prize = prize


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    manger1 = GardenManager()
    garden1 = GardenManager.create_garden(manger1, "Alice")
    garden2 = GardenManager.create_garden(manger1, "Bob")

    plant1 = Plant("Oak Tree", 100)
    flower1 = FloweringPlant("Rose", 25, "red", True)
    prize1 = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    prize2 = PrizeFlower("Nightflower", 52, "black", False, 10)

    garden1.add_plant(plant1)
    garden1.add_plant(flower1)
    garden1.add_plant(prize1)

    garden2.add_plant(prize2)

    print("")

    garden1.plants_grow()

    print("")

    print("=== Alice's Garden Report ===")

    stats1 = manger1.GardenStats(garden1)
    stats1.plants_stats()

    print("")

    stats1.added_and_growth()
    stats1.plants_type()

    print("")

    GardenManager.validate_height(plant1.height)
    manger1.create_garden_network()
    GardenManager.total_gardens_managed()


if __name__ == "__main__":
    main()
