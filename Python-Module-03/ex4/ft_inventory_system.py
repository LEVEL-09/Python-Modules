import sys


def main() -> None:
    if len(sys.argv) <= 1:
        print("No item!!!")
        return

    print("=== Inventory System Analysis ===")
    try:
        inventory = {}
        most = {}
        least = {}
        for i in sys.argv[1:]:
            args_list = i.split(":")
            inventory.update({
                args_list[0]: {
                    "type": "unknown",
                    "quantity": int(args_list[1]),
                    "value": 0
                }
            })

        most[args_list[0]] = int(args_list[1])
        least[args_list[0]] = int(args_list[1])

        unique_items = 0
        for key, value in inventory.items():
            if value.get("quantity") > [i for i in most.values()][0]:
                most = {}
                most.update({key: value.get("quantity")})
            if value.get("quantity") < [i for i in least.values()][0]:
                least = {}
                least.update({key: value.get("quantity")})
            unique_items += value.get("quantity")

        print(f"Total items in inventory: {unique_items}")
        print(f"Unique item types: {len(inventory)}")

        print("\n=== Current Inventory ===")
        temp_inventory = inventory.copy()
        while temp_inventory:
            for max_key in temp_inventory:
                break
            for key in temp_inventory:
                key_data = temp_inventory.get(key).get("quantity")
                max_data = temp_inventory.get(max_key).get("quantity")
                if key_data > max_data:
                    max_key = key
            value = temp_inventory.get(max_key).get("quantity")
            units = (value/unique_items)*100
            print(f"{max_key}: {value} units ({units:.1f}%)")
            temp_inventory.pop(max_key)

        print("\n=== Inventory Statistics ===")
        for most_key, most_value in most.items():
            print(f"Most abundant: {most_key} ({most_value} units)")
        for least_key, least_value in least.items():
            print(f"Least abundant: {least_key} ({least_value} unit)")

        print("\n=== Item Categories ===")
        abundant = {}
        moderate = {}
        scarce = {}
        restock = []
        for key, value in inventory.items():
            if value.get("quantity") >= 10:
                abundant.update({key: value})
            elif value.get("quantity") >= 5:
                moderate.update({key: value})
            else:
                if value.get("quantity") == 1:
                    restock.append(key)
                scarce.update({key: value})
        if abundant:
            print("Abundant:", {k: v["quantity"] for k, v in abundant.items()})
        if moderate:
            print("Moderate:", {k: v["quantity"] for k, v in moderate.items()})
        if scarce:
            print("Scarce:", {k: v["quantity"] for k, v in scarce.items()})

        print("\n=== Management Suggestions ===")
        print("Restock needed:", ", ".join(restock))

        print("\n=== Dictionary Properties Demo ===")

        print("Dictionary keys: ", end="")
        print(*inventory, sep=", ")

        print("Dictionary values: ", end="")
        print(
            *(data.get("quantity") for data in inventory.values()),
            sep=", "
        )

        lookup = "sword"
        if lookup in inventory:
            print(f"Sample lookup - '{lookup}' in inventory: True")
        else:
            print(f"Sample lookup - '{lookup}' in inventory: False")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
