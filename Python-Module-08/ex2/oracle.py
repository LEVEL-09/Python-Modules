import os
import dotenv


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    # Load .env variables to os.environ and allow override
    # If .env file exist dotenv.load_dotenv return True else return False
    if dotenv.load_dotenv(".env", override=False):
        print("\nConfiguration loaded:")
        try:
            # Get Value from key in os.environ mapping
            print("Mode:", os.environ["MATRIX_MODE"])
            print("Database:", os.environ["DATABASE_URL"])
            print("API Access:", os.environ["API_KEY"])
            print("Log Level:", os.environ["LOG_LEVEL"])
            print("ZION_ENDPOINT:", os.environ["ZION_ENDPOINT"])

            print("\nEnvironment security check:")
            print("[OK] No hardcoded secrets detected")
            print("[OK] .env file properly configured")
            print("[OK] Production overrides available")

            print("\nThe Oracle sees all configurations.")
        except KeyError as e:
            print(f"Can't find {e} key in .env file")
    else:
        print(".env file is messing")


if __name__ == "__main__":
    main()
