"""
operaatorite_ylelaadimine.py

Näide klassi abil operaatori ülelaadimisest
"""
#
# Esmane näide
#

class Ruut:
    def __init__(self, külgi):
        self.külgi = külgi

ruut1 = Ruut(5)    #  5 * 4 külge = 20
ruut2 = Ruut(10)   # 10 * 4 külge = 40
print(f"Ruutude külgede summa on {ruut1 + ruut2}")   # Saame vea!!

#
# Parandatud näide
#

class RuutB:
    def __init__(self, külgi):
        self.külgi = külgi

    def __add__(ruut1, ruut2):
        return ((4 * ruut1.külgi) + (4 * ruut2.külgi))

ruut1 = RuutB(5)    #  5 * 4 külge = 20
ruut2 = RuutB(10)   # 10 * 4 külge = 40
print(f"Ruutude külgede summa on {ruut1 + ruut2}")   # Tulemus: 60

#
# Decimal näide
#

y = 0.1 + 0.1 + 0.1 - 0.3
print(y)    # Tulemuseks: 5.551115123125783e-17

from decimal import *

a = Decimal('.10')
b = Decimal('.30')

x = a + a + a - b
print(x)           # Tulemus 0.00


#
# Itereeritava klassi loomine
#

class Loendur:
    def __init__(self, low, high):
        self._current = low
        self._high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._high:
            raise StopIteration
        else:
            self._current += 1
            return self._current - 1
    
# Kasutamine
for c in Loendur(3, 7):
    print(c)

#
# Sama asi generaatori abil
#

def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1

# Kasutamine
for c in counter(3, 8):
    print(c)

