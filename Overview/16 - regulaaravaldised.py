"""
regulaaravaldised.py

Mõned regulaaravaldiste näide
"""

import re

muster = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"  # alternatiivne r"[^@]+@[^@]+\.[^@]+"

while True:
    sisend = input("Sisesta emaili aadress: ")

    if len(sisend) == 0:
        break

    if re.match(muster, sisend):
        print("Korrektne email")
    else:
        print("Vigane email")
