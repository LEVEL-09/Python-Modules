from typing import Tuple, List
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise ValueError("Both arguments must be callable")

    def cast_combined_spells(target: str, power: int) -> Tuple:
        return (spell1(target, power), spell2(target, power))

    return cast_combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise ValueError("First argument must be callable")
    if not isinstance(multiplier, int):
        raise ValueError("Second argument must be an integer")

    def apply_power_to_target(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return apply_power_to_target


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise ValueError("Both arguments must be callable")

    def cast_conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast_conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise ValueError("All elements in the list must be callable")

    def apply_magic_powers(target: str, power: int) -> List[str]:
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result

    return apply_magic_powers


print("\nTesting spell combiner...")
try:
    def fireball(target: str, power: int) -> str:
        return f"Abrakadabra {target} for {power} AT"

    def heal(target: str, power: int) -> str:
        return f"Abrakadabra {target} for {power} HP"

    fun = spell_combiner(fireball, heal)
    print("Combined spell result:", *fun("Dragon", 7))

    print("\nTesting power amplifier...")
    power = 10
    fun = power_amplifier(fireball, power)

    print(f"Original: {fireball('Goblin', power)}",
          f"Amplified: {fun('Goblin', power)}")
except ValueError as e:
    print("Error:", e)
