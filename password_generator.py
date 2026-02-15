import random


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};:,.?/"

    pool = ""
    if use_letters:
        pool += letters
    if use_numbers:
        pool += numbers
    if use_symbols:
        pool += symbols

    if not pool:
        return ""

    password = ""
    for _ in range(length):
        password += random.choice(pool)

    return password


def main():
    print("Simple Password Generator")
    length = int(input("Enter password length: "))

    use_letters = input("Use letters? (y/n): ").strip().lower() == "y"
    use_numbers = input("Use numbers? (y/n): ").strip().lower() == "y"
    use_symbols = input("Use symbols? (y/n): ").strip().lower() == "y"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Your password:", password)
    else:
        print("You did not choose any character types.")


if __name__ == "__main__":
    main()
