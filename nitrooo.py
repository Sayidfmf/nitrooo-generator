import random
import time

# --- Luhn Algorithm ---
def luhn_check(card_number):
    digits = [int(d) for d in card_number[::-1]]
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled - 9 if doubled > 9 else doubled
        else:
            total += digit
    return total % 10 == 0

def generate_card_number(start_digit, total_length):
    while True:
        number_length = total_length - len(start_digit) - 1  # Leave space for check digit
        body = start_digit + ''.join(random.choices('0123456789', k=number_length))
        for check_digit in range(10):
            candidate = body + str(check_digit)
            if luhn_check(candidate):
                return candidate

# --- Fake Code Redemption System ---
valid_codes = {
    "FREE2025": "10% Discount",
    "WELCOME50": "$5 Credit",
    "GOLD123": "1 Month Premium"
}

def redeem_code(code):
    code = code.strip().upper()
    if code in valid_codes:
        return f"✅ Code Redeemed: {valid_codes[code]}"
    else:
        return "❌ Invalid or Expired Code"

# --- Main Menu ---
def main():
    print("\033[1;31m== BY SOLRA TOOLS ==")
    print("== discord: solra0478 ==\033[0m")
    print("====== MULTI TOOL ======")
    print("1. Generate Card Numbers")
    print("2. Check Card Number Validity")
    print("3. Redeem a Code")
    print("==========================")

    mode = input("Choose mode (1-3): ")

    if mode == "1":
        print("\nCard Types:")
        print("1. VISA")
        print("2. MasterCard")
        print("3. American Express")
        print("=======================")

        choice = input("Choose card type (1-3): ")
        card_types = {
            "1": ("VISA", "4", 16),
            "2": ("MasterCard", "5", 16),
            "3": ("Amex", "3", 15)
        }

        if choice in card_types:
            try:
                amount = int(input("How many cards to simulate?: "))
                card_name, start_digit, length = card_types[choice]
                print(f"\nGenerating {amount} {card_name} cards...\n")
                time.sleep(1)
                for _ in range(amount):
                    card_number = generate_card_number(start_digit, length)
                    exp_month = str(random.randint(1, 12)).zfill(2)
                    exp_year = str(random.randint(25, 30))
                    cvv_length = 4 if card_name == "Amex" else 3
                    cvv = ''.join(random.choices('0123456789', k=cvv_length))
                    print(f"{card_number} | {exp_month}/{exp_year} | CVV: {cvv} | Valid")
                    time.sleep(0.2)
            except ValueError:
                print("\nInvalid number entered.")
        else:
            print("\nInvalid card type choice.")

    elif mode == "2":
        user_card = input("Enter card number to check: ").strip()
        if user_card.isdigit():
            if luhn_check(user_card):
                print(f"\n{user_card} is VALID ✅")
            else:
                print(f"\n{user_card} is INVALID ❌")
        else:
            print("\nInvalid input — only digits allowed.")

    elif mode == "3":
        code = input("Enter redeem code: ")
        result = redeem_code(code)
        print(result)

    else:
        print("\nInvalid mode selected.")

if __name__ == "__main__":
    main()
