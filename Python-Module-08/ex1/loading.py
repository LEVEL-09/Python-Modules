# Check version of all dependencies is correct
def check_dependencies() -> None:
    print("\nChecking dependencies:")
    packages = {
        pandas: "Data manipulation",
        requests: "Network access",
        matplotlib: "Visualization",
        numpy: "numerical computations"
    }
    for key, value in packages.items():
        if key.__name__ == "pandas" and key.__version__ == "2.1.0":
            print(f"[OK] {key.__name__} ({key.__version__}) - {value}"
                  f" ready")
        elif key.__name__ == "requests" and key.__version__ == "2.31.0":
            print(f"[OK] {key.__name__} ({key.__version__}) - {value}"
                  f" ready")
        elif key.__name__ == "matplotlib" and key.__version__ == "3.7.2":
            print(f"[OK] {key.__name__} ({key.__version__}) - {value}"
                  f" ready")
        elif key.__name__ == "numpy" and key.__version__ == "1.26.4":
            print(f"[OK] {key.__name__} ({key.__version__}) - {value}"
                  f" ready")
        else:
            raise ImportWarning(f"Waring {key.__name__} version")


def main() -> None:
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York',
                 'Los Angeles'],
        'Salary_USD': [50000, 60000, 70000, 55000, 45000]
    }
    # Create table from data use DataFrame
    df = pandas.DataFrame(data)

    url = 'https://www.google.com/'
    # Send request to google.com
    response = requests.get(url)

    xpoints = numpy.array([1, 8])
    ypoints = numpy.array([3, 10])
    # Create plot use x and y direction from array created by numpy
    # Save it as png image
    matplotlib.pyplot.plot(xpoints, ypoints)
    matplotlib.pyplot.savefig("matrix_analysis.png")

    print("\n", df)
    print(f"\nStatus Code: {response.status_code}")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    # Check if dependencies install by catch ImportError
    try:
        import pandas
        import requests
        import matplotlib.pyplot
        import numpy

        check_dependencies()
        main()
    except ImportError:
        print("Dependencies is NOT installed. Please install it")
    except Exception as e:
        print(e)
