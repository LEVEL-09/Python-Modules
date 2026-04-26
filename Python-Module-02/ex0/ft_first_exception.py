#! /usr/bin/env python3

def check_temperature(temp_str: str) -> None | int:
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number\n")

    if temperature > 40:
        raise ValueError(f"Error: {temperature}°C is too hot for plants "
                         "(max 40°C)\n")
    elif temperature < 0:
        raise ValueError(f"Error: {temperature}°C is too cold for plants "
                         "(min 0°C)\n")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!\n")
        return temperature


def test_temperature_input() -> None:
    print("Testing temperature: 25")
    try:
        check_temperature("25")
    except Exception as e:
        print(e)

    print("Testing temperature: abc")
    try:
        check_temperature("abc")
    except Exception as e:
        print(e)

    print("Testing temperature: 100")
    try:
        check_temperature("100")
    except Exception as e:
        print(e)

    print("Testing temperature: -50")
    try:
        check_temperature("-50")
    except Exception as e:
        print(e)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    try:
        test_temperature_input()
    except Exception as e:
        print(e)
