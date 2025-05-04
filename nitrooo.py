import random

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

def generate_visa():
    return generate_card_number("4", 16)

def generate_mastercard():
    prefixes = [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]
    prefix = random.choice(prefixes)
    return generate_card_number(prefix, 16)

def print_header(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

def main_menu():
    while True:
        print_header("Card Generator & Validator")
        print("1. Generate Visa Card")
        print("2. Generate Mastercard")
        print("3. Check Card Validity")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            card = generate_visa()
            print(f"Generated Visa Card: {card}")
        elif choice == "2":
            card = generate_mastercard()
            print(f"Generated Mastercard: {card}")
        elif choice == "3":
            card = input("Enter card number to check: ").strip()
            if card.isdigit():
                valid = is_luhn_valid(card)
                print(f"Card {card} is {'valid' if valid else 'invalid'}.")
            else:
                print("Invalid input. Please enter only digits.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
