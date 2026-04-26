if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        file_name = "ancient_fragment.txt"

        print(f"Accessing Storage Vault: {file_name}")
        fo = open(file_name, 'r')

        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(fo.read())

        fo.close()

        print("\nData recovery complete. Storage unit disconnected.")
    except OSError:
        print("ERROR: Storage vault not found. Run data generator first")
