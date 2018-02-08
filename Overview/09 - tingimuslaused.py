"""
tingimuslaused.py

Erinevad võimalused teingimuste esitamiseks
"""

#
# Lihtne tingimuslause
#

if 2 < 5:
    print("2 on väiksem kui 5")
else:
    print("2 ei ole väiksem kui 5")

#
# Tingimused muutujaga
#

# Esimene variant

x = 2

if (x > 0):
    print("Positiivne")
else:
    print("Negatiivne")


# Proovime sama asja nulliga
x = 0

if (x > 0):
    print("Positiivne")
else:
    print("Negatiivne")


# Parandatud variant

if (x > 0):
    print("Positiivne")
else:
    if (x == 0):
        print("Null")
    else:
        print("Negatiivne")

# Veelgi parem variant

if (x > 0):
    print("Positiivne")
elif (x == 0):
    print("Null")
else:
    print("Negatiivne")

# Võimalikud tingimused:
# < – Väikse kui
# > – Suurem kui
# <= – Väiksem või võrdne
# >= – Suurem või võrdne
# == – Võrdne
# != – Mittevõrdne
#
# Lisaks tingimuste ühendamine and, or ja not abil

x = 2

print(x == 3 or x < 2 and not x >= 5)