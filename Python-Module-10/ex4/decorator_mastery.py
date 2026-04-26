from collections.abc import Callable
from functools import wraps
from time import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> str:
        print(f"Casting {func.__name__}...")

        start = time()
        func(*args)
        end = time()

        print(f"Spell completed in {end - start:.3f} seconds")
        return f"{args[0]} cast!"

    return wrapper


print("Testing spell timer...")


@spell_timer
def fireball(arg: str) -> None:
    pass


print("Result:", fireball("Fireball"))


def power_validator(min_power: int) -> Callable:
    def decorator_factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args) -> str:
            if args[-1] < min_power:
                return "Insufficient power for this spell"
            return func(*args)

        return wrapper
    return decorator_factory


print("\nTesting power validator...")


@power_validator(10)
def iceball(arg: int) -> str:
    return "Attack"


print("Result:", iceball(11))


def retry_spell(max_attempts: int) -> Callable:
    def decorator_factory(func: Callable) -> Callable:
        n = 1

        @wraps(func)
        def wrapper(*args) -> str:
            nonlocal n

            try:
                return func(n)
            except Exception:
                print(f"Spell failed, retrying... ({n}/{max_attempts})")
                if n < max_attempts - 1:
                    n = n + 1
                    return wrapper()
                return f"Spell casting failed after {max_attempts}"

        return wrapper
    return decorator_factory


print("\nTesting retrying spell...")


@retry_spell(3)
def the_answer(arg: int) -> str:
    if arg != 3:
        raise Exception("Nice Try")
    return "Waaaaaaagh spelled !"


print(the_answer(), "attempts")


@retry_spell(4)
def the_answer2(arg: int) -> str:
    if arg != 1:
        raise Exception("Nice Try")
    return "Waaaaaaagh spelled !"


print(the_answer2())


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and \
           all(c.isspace() or c.isalpha() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


print("\nTesting MageGuild...")
mageguild_instance = MageGuild()
print(mageguild_instance.validate_mage_name("Dragon"))
print(mageguild_instance.validate_mage_name("Ax"))

print(mageguild_instance.cast_spell("KHOFACH", 15))
print(mageguild_instance.cast_spell("Nizak", 4))
