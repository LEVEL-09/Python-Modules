#! /usr/bin/env python3

def garden_operations(data: str | int) -> None:
    result = 0
    result = int(data)

    10 / result

    dictionary = {1: "one", 2: "two", 5: "five"}
    dictionary[result]

    if result != 5:
        file = open("missing.txt")
        file.close()

    if result == 5:
        list_num = [1, 2, 3, 4]
        list_num[result]


def test_error_types() -> None:
    try:
        print("Testing ValueError...")
        garden_operations("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations(0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations(1)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden_operations(3)
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        garden_operations(5)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError,
            IndexError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")

    try:
        test_error_types()
    except Exception as e:
        print(e)
