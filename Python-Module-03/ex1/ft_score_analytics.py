import sys


def score() -> None:
    if len(sys.argv) <= 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        args = []
        for i in sys.argv[1:]:
            arg = i
            args += [int(i)]
        total = len(sys.argv) - 1
        total_score = sum(int(num) for num in sys.argv[1:])
        average_score = int(total_score)/total
        max_num = int(max(sys.argv[1:]))
        min_num = int(min(sys.argv[1:]))
        print(f"Scores processed: {args}")
        print(f"Total players: {total}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {max_num}")
        print(f"Low score: {min_num}")
        print(f"Score range: {max_num - min_num}\n")
    except ValueError:
        print(f"oops, I typed ’{arg}’ instead of ’1000’")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score()
