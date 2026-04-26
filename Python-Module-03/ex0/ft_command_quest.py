import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    total = len(sys.argv)

    if total == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")
    x = 1
    if total > 1:
        print(f"Arguments received: {total - 1}")
        for i in sys.argv:
            if i == sys.argv[0]:
                continue
            print(f"Argument {x}: {i}")
            x += 1

    print(f"Total arguments: {total}\n")
