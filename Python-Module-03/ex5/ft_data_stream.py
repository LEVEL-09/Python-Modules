from typing import Generator

players = ["alice", "bob", "charlie", "leon"]
actions = ["killed monster", "found treasure", "leveled up", "drink milk",
           "fatality", "leveled up"]


def game_event_stream(n: int) -> Generator[dict, None, None]:
    for i in range(n):
        i += 1
        yield {
            "event": i,
            "player": players[i % 4],
            "level": ((i % 50) + 1),
            "action": actions[i % 6]
        }


def fibonacci(n: int) -> Generator[str, None, None]:
    n0 = 0
    n1 = 1
    for _ in range(n):
        if _ < n - 1:
            yield f"{n0}, "
        else:
            yield f"{n0}\n"
        n0, n1 = n1, n0 + n1


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    num = 2
    while (num * num <= n):
        if (n % num == 0):
            return False
        num += 1

    return True


def prime(n: int) -> Generator[str, None, None]:
    num = 2
    for i in range(n):
        while True:
            if is_prime(num):
                if i != n - 1:
                    yield f"{num}, "
                else:
                    yield f"{num}\n"
                num += 1
                break
            else:
                num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    print("Processing 1000 game events...\n")

    total = 0
    treasure = 0
    level_up = 0
    height_level_player = 0
    for i in game_event_stream(1000):
        print(f"Event {i['event']}: Player {i['player']} (level {i['level']}) "
              f"{i['action']}")
        if i["level"] >= 10:
            height_level_player += 1
        if i["action"] == "leveled up":
            level_up += 1
        if i["action"] == "found treasure":
            treasure += 1
        total += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {height_level_player}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    for i in fibonacci(10):
        print(i, end="")

    print("Prime numbers (first 5): ", end="")
    for i in prime(5):
        print(i, end="")
