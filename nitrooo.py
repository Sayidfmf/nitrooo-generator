import random
import time
print("\033[1;31m== BY SOLRA TOOLS ==")
print("== discord: solra0478 ==\033[0m")
print("====== CREDIT CARD GENERATOR ======")
print("1. VISA")
print("2. MasterCard")
print("3. American Express")
print("=====================================")
choice = input("Choose card type (1-3): ")
card_types = {
 "1": ("VISA", "4"),
 "2": ("MasterCard", "5"),
 "3": ("Amex", "3")
}
if choice in card_types:
 try:
 amount = int(input("How many cards to generate?: "))
 card_name, start_digit = card_types[choice]
 print(f"\nGenerating {amount} {card_name} cards...\n")
 time.sleep(1)
 for _ in range(amount):
 card_number = start_digit + ''.join(random.choices('0123456789', k=15))
 exp_month = str(random.randint(1, 12)).zfill(2)
 exp_year = str(random.randint(25, 30))
 cvv = ''.join(random.choices('0123456789', k=3))
 print(f"{card_number} | {exp_month}/{exp_year} | CVV: {cvv}")
 time.sleep(0.2)
 except ValueError:
 print("\nInvalid number entered.")
else:
 print("\nInvalid card type choice.")
