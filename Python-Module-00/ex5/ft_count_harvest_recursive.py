def recursive(days: int, i: int) -> None:
    if (days > 0):
        print(f"Day {i}")
        recursive(days - 1, i + 1)


def ft_count_harvest_recursive() -> None:
    recursive(int(input("Days until harvest: ")), 1)
    print("Harvest time!")
