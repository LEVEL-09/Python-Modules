import math


def print_xyz(x: int, y: int, z: int) -> None:
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    p1 = (10, 20, 5)
    p2 = (0, 0, 0)

    x1, y1, z1 = p1
    x2, y2, z2 = p2
    try:
        position = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"Position created: {p1}")
        print(f"Distance between {p2} and {p1}: {position:.2f}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    try:
        coord_str = "3,4,0"
        coord_tuple = tuple(int(i) for i in coord_str.split(","))
        x1, y1, z1 = coord_tuple
        print(f"Parsing coordinates: \"{coord_str}\"")
        print(f"Parsed position: {coord_tuple}")
        position = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"Distance between {p2} and {coord_tuple}: "
              f"{position:.2f}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    try:
        coord_str = "abc,def,ghi"
        print(f"Parsing invalid coordinates: \"{coord_str}\"")
        x1, y1, z1 = tuple(int(i) for i in coord_str.split(","))
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    try:
        x, y, z = (3, 4, 0)
        print(f"Player at x={x}, y={y}, z={z}")

        xyz = (3, 4, 0)
        print_xyz(*xyz)
    except Exception as e:
        print(e)
