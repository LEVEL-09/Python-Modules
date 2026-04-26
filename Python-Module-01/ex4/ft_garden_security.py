#! /usr/bin/env python3

class Plant:
    """Class for plants object"""
    def __init__(self: object, name: str) -> None:
        """plants name"""
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def get_height(self: object) -> int:
        return (self._height)

    def get_age(self: object) -> int:
        return (self._age)

    def set_height(self: object, height: int) -> None:
        self.SecurePlant(height, "height")

    def set_age(self: object, age: int) -> None:
        self.SecurePlant(age, "age")

    def SecurePlant(self: object, value: int, field: str) -> None:
        if (value < 0):
            if (field == "height"):
                print(f"Invalid operation attempted: {field} {value}cm "
                      f"[REJECTED]")
                print("Security: Negative height rejected")
            elif (field == "age"):
                print(f"Invalid operation attempted: {field} {value} days "
                      f"[REJECTED]")
                print("Security: Negative age rejected")
        else:
            if (field == "height"):
                print(f"{field.capitalize()} updated: {value}cm [OK]")
                self._height = value
            elif (field == "age"):
                print(f"{field.capitalize()} updated: {value} days [OK]")
                self._age = value


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose")
    plant1.set_height(25)
    plant1.set_age(30)
    print("")
    plant1.set_height(-5)
    print("")
    print(f"Current plant: {plant1.name} ({plant1.get_height()}cm,"
          f" {plant1.get_age()} days)")
