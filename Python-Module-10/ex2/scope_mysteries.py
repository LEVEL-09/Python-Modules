from collections.abc import Callable


def mage_counter() -> Callable:
    counts = 0

    def count() -> int:
        nonlocal counts
        counts += 1
        return counts
    return count


def spell_accumulator(initial_power: int) -> Callable:
    mount = 0

    def accumulate(add: int) -> int:
        nonlocal mount
        mount += add
        return mount + initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: int) -> str:
        vault[key] = value
        return f"'{key}' = {value}"

    def recall(key: str) -> str:
        if key not in vault:
            return f"'{key}': Memory not found"
        return f"'{key}': {vault[key]}"

    return {
        "Store": store,
        "Recall": recall
    }


print("Testing mage counter...")
counter_a = mage_counter()
counter_b = mage_counter()
print("counter_a call 1", counter_a())
print("counter_a call 2", counter_a())
print("counter_b call 1", counter_b())

print("\nTesting spell accumulator...")
accumulator_a = spell_accumulator(100)
print("Base 100, add 20:", accumulator_a(20))
print("Base 100, add 30:", accumulator_a(30))

print("\nTesting enchantment factory...")
anchor_enchant = enchantment_factory("Flaming")
print(anchor_enchant("Sword"))
anchor_enchant = enchantment_factory("Frozen")
print(anchor_enchant("Shield"))

print("\nTesting memory vault...")
vault = memory_vault()
store = vault["Store"]
print("Store", store("secret", 42))
recall = vault["Recall"]
print("Recall", recall("secret"))
print("Recall", recall("unknown"))
