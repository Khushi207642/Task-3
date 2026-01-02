from port_scanner import scan_ports
from brute_forcer import brute_force_demo

def menu():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Force Demo")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        host = input("Enter host (default 127.0.0.1): ")
        if host == "":
            host = "127.0.0.1"
        ports = scan_ports(host)
        print("Open ports:", ports)

    elif choice == "2":
        brute_force_demo("test123")

    elif choice == "3":
        print("Exiting toolkit...")
        break

    else:
        print("Invalid choice. Try again.")
