#!/usr/bin/env python3
import random

# Colors for terminal output
RED = '\033[1;31m'
GRN = '\033[0;32m'
NC = '\033[0m'

print(f"{RED}Rewe Logs Generator - BY SOLRA{NC}\n")

# Ask how many logs
amount = input("How many REWE logs to generate? > ")
try:
    amount = int(amount)
except ValueError:
    print("Please enter a valid number.")
    exit(1)

names = [
    ("Jonas", "Becker"),
    ("Nico", "Keller"),
    ("Tom", "Meier"),
    ("Lukas", "Neumann"),
    ("Felix", "Brandt"),
    ("Sophie", "Koch"),
    ("Laura", "Richter"),
    ("Anna", "Hofmann"),
    ("Marie", "Lang"),
    ("Lea", "Scholz"),
]

domains = ["gmail.com", "icloud.com"]

for i in range(1, amount + 1):
    rand_id = random.randint(0, 999)
    points = random.randint(1000, 50000)

    first, last = random.choice(names)
    domain = random.choice(domains)
    email = f"{first}.{last}{rand_id}@{domain}".lower()

    password_type = random.randint(0, 3)
    if password_type == 0:
        password = f"{first}{random.randint(0, 9999)}%"
    elif password_type == 1:
        password = f"{first}{last}!{random.randint(0, 99)}"
    elif password_type == 2:
        password = f"{first}2024!"
    else:
        password = f"Rewe{random.randint(0, 9999)}"

    if random.randint(0, 1) == 0:
        prefix = "+49 157"
        number = random.randint(1000000, 9999999)
        phone = f"{prefix} {number}"
    else:
        area = random.randint(200, 999)
        exchange = random.randint(100, 999)
        line = random.randint(1000, 9999)
        phone = f"+1 {area}-{exchange}-{line}"

    print(f"{RED}[{i}] Name:{NC} {first} {last}")
    print(f"{RED}    Email:{NC} {email}")
    print(f"{RED}    Password:{NC} {password}")
    print(f"{RED}    Phone:{NC} {phone}")
    print(f"{RED}    Payback Points:{NC} {points}")
    print(f"{GRN}    [+] Account Status: VERIFIED{NC}\n")
