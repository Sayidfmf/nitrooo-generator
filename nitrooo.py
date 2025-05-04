import random
from datetime import datetime, timedelta

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def generate_card_number(prefix, length):
    number = prefix
    while len(number) < (length - 1):
        number += str(random.randint(0,9))
    checksum = luhn_checksum(int(number) * 10)
    check_digit = (10 - checksum) % 10
    return number + str(check_digit)

def generate_cvv():
    # CVV is a random 3-digit number for Visa and Mastercard
    return str(random.randint(100, 999))

def generate_expiration_date():
    # Hardcoded current date to May 4, 2025, based on system info
    # Generates a future expiration date between now and 5 years ahead
    now = datetime(2025, 5, 4)
    future_date = now + timedelta(days=random.randint(1, 1825))  # 1825 days ≈ 5 years
    exp_month = future_date.month
    exp_year = future_date.year % 100  # YY format
    return f"{exp_month:02d}/{exp_year:02d}"

def generate_visa():
    card_number = generate_card_number("4", 16)
    cvv = generate_cvv()
    expiration = generate_expiration_date()
    return card_number, cvv, expiration

def generate_mastercard():
    prefixes = [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]
    prefix = random.choice(prefixes)
    card_number = generate_card_number(prefix, 16)
    cvv = generate_cvv()
    expiration = generate_expiration_date()
    return card_number, cvv, expiration

def print_header(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

def main_menu():
    while True:
        print_header("Card Generator & Validator")
        print("1. Generate Visa Card (with CVV and Expiration)")
        print("2. Generate Mastercard (with CVV and Expiration)")
        print("3. Check Card Validity (Luhn check only)")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            card_number, cvv, expiration = generate_visa()
            print(f"Generated Visa Card: Number: {card_number}, CVV: {cvv}, Expiration: {expiration}")
        elif choice == "2":
            card_number, cvv, expiration = generate_mastercard()
            print(f"Generated Mastercard: Number: {card_number}, CVV: {cvv}, Expiration: {expiration}")
        elif choice == "3":
            card_input = input("Enter card number to check (ignore CVV/Expiration): ").strip()
            if card_input.isdigit():
                valid = is_luhn_valid(card_input)
                print(f"Card {card_input} is {'valid' if valid else 'invalid'} (based on Luhn algorithm).")
            else:
                print("Invalid input. Please enter only digits for the card number.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
