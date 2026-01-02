# Educational brute force demo (NOT real hacking)

def brute_force_demo(correct_password):
    password_list = ["1234", "admin", "password", "test123", "letmein"]

    print("\nStarting brute force demo...")
    for pwd in password_list:
        print(f"Trying password: {pwd}")
        if pwd == correct_password:
            print(f"Password found: {pwd}")
            return pwd

    print("Password not found")
    return None


if __name__ == "__main__":
    brute_force_demo("test123")
