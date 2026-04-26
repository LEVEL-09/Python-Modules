import sys
import os
import site


def main() -> None:
    # Check the directory of python interpreter
    if sys.prefix == sys.base_prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")

        # Executable file on a computer's file system
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("""\nWARNING: You're in the global environment!
The machines can see everything you install.""")

        print("""\nTo enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows

Then run this program again.""")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        # Returns the last component (the "basename") of the path
        # That points to your Python installation directory
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        # String that indicates the site-specific directory prefix where
        # Platform-independent Python files and modules are installed
        print(f"Environment Path: {sys.prefix}")

        print("""\nSUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.""")

        # Global site-packages directories
        print(f"\nPackage installation path:\n{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
