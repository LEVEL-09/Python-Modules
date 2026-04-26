if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...\nVault connection "
          "established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open("classified_data.txt", 'r') as fo:
        print(fo.read())

    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", 'w') as fo:
        fo.write("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")

    with open("security_protocols.txt", 'r') as fo:
        print(fo.read())

    print("\nAll vault operations completed with maximum security.")
