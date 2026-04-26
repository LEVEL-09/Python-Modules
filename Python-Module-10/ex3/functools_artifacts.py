from typing import Any
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator


ops = {
    "add": operator.add,
    "multiply": operator.mul,
    "max": max,
    "min": min
}


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    total = reduce(ops[operation], spells)
    return total


print("\nTesting spell reducer...")
try:
    print("Sum:", spell_reducer([10, 20, 30, 40], "add"))
    print("Product:", spell_reducer([10, 20, 30, 40], "multiply"))
    print("Max:", spell_reducer([10, 20, 30, 40], "max"))
except KeyError as e:
    print(f"Operator {e} is unknown")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantment_v1 = partial(base_enchantment, 50, "Fire")
    enchantment_v2 = partial(base_enchantment, 50, "Love")
    enchantment_v3 = partial(base_enchantment, 50, "Ice")

    return {
        "enchantment v1": enchantment_v1,
        "enchantment v2": enchantment_v2,
        "enchantment v3": enchantment_v3
    }


def base_enchantment_function(power: int, element: str,
                              target: str) -> str:
    return f"attack {target} by {power} damage use {element}"


print("\nTesting partial enchanter...")
try:
    bases = partial_enchanter(base_enchantment_function)
    print(bases["enchantment v1"]("Dragon"))
    print(bases["enchantment v2"]("Goblin"))
    print(bases["enchantment v3"]("Witch"))
except KeyError as e:
    print(f"enchantment {e} is unknown")


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


print("\nTesting memoized fibonacci...")
print("Fib(0):", memoized_fibonacci(0))
print("Fib(1):", memoized_fibonacci(1))
print("Fib(10):", memoized_fibonacci(10))
print("Fib(15):", memoized_fibonacci(15))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell_system(arg) -> str:
        return "Unknown spell type"

    @spell_system.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell_system.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell_system.register
    def _(arg: list) -> str:
        spell_total = len(arg)
        return f"Multi-cast: {spell_total} spells"

    return spell_system


print("\nTesting spell dispatcher...")
fun = spell_dispatcher()
print(fun(42))
print(fun("fireball"))
print(fun([spell_reducer, partial_enchanter, base_enchantment_function]))
print(fun(3.3))
