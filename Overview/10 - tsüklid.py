"""
tsüklid.py

Vahendid listide jt mitme-elemendiliste konstruktsioonide läbi käimiseks
"""

#
# FOR-tsükkel
#

list = ["Element 1", 2, "Element 3", True, "Element 5"]

for element in list:
    print(element)

# Numbrite trükkimine range() funktsiooni abil
for i in range(0, 10):
    print(i)
        
# Numbrite trükkimine range() funktsiooni abil koos sammuga
# Praegu trükime välja kõik paaris arvud
for i in range(0, 101, 2):
    print(i)
    

#
# WHILE tsükkel
#

x = 0

while x < 10:
    print(x)
    x = x + 1

#
# Juhtkäsud: continue, break ja pass
#

# Trükime välja paaris arvud (vigane)
x = 0

while x < 102:
    if (x % 2 != 0):
        continue
    print(x)
    x = x + 1

    if x == 100:
        break
    else:
        pass

# Parandatud variant
x = 0

while x < 102:
    x = x + 1
    if (x % 2 != 0):
        continue
    print(x)

    if x == 100:
        break
    else:
        pass


# Üks võimalik algarvude generaatori variant
# https://en.wikipedia.org/wiki/Prime_number
# https://stackoverflow.com/questions/18833759/python-prime-number-checker

# Esmalt jookseme läbi arvud vahemikus 1..100. 
# Kui arvu on 1 või jagub kahega (kui on suurem kui 2), siis võime kohe järgmise numbri juurde minna. 
# Edasi käime läbi kõik arvud 3-st kuni antud arvuni ja vaatame, kas soovitud arv jagub teise arvuga 
# ilma jäägita. Kui jagub, siis ei ole algarv ja võime sisemise tsükli lõpetada. Lõpuks trükime teate
# kui arv oli algarv.

for n in range(1, 100):        # Genereerime numbrid vahemikus 1..100
    # Kui tegu on paarisarvuga, mis on suurem kui 2, või number == 1, 
    # siis võime selle vahele jätta
    if (n % 2 == 0 and n > 2) or n == 1: 
        continue

    is_prime = True            # Eeldame, et meil on tegu algarvuga
    for i in range(2, n):      # Läbime vahemiku 3..n (hetkel vaadeldav arv)
        if n % i == 0:         # Kui vaadeldav arv jagub mõne väiksemaga...
            is_prime = False   # ... siis ei ole tegu algarvuga
            break

    if is_prime:               # Kui oli algarv, trükime selle välja
        print(str(n) + " on algarv")
        

# Tsükkel sisendi saamiseks
while True:
    sisend = input("Palun sisesta number. Tsükli lõpetamiseks vajuta ENTER: ")

    if len(sisend) == 0:
        break

    print("Sa trükkisid: " + sisend)

# Fibonacci jada teada saamine
a, b = 0, 1
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b
print() # Lisame reavahetuse
