if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt") as fo:
            pass
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix\n"
              "STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt") as fo:
            pass
    except PermissionError:
        print("RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", 'r') as fo:
            print(F"SUCCESS: Archive recovered - ``{fo.read()}''")
            print("STATUS: Normal operations resumed")
    except Exception as e:
        print(e)

    print("\nAll crisis scenarios handled successfully. Archives secure.")
