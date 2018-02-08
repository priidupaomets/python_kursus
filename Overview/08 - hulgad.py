"""
tuhulgadple.py

Hulkade defineerimine ja operatsioonid nende peal
"""

#
# Deklareerimine
#

# Tühja hulga deklareerimine
hulk = set()
print(hulk)

# hulk, milles on mõned elemendid(osad neist topelt)
ostukorv = { "Õunad", "Kartulid", "Makaronid", "Õunad", "Sidrunid", "Kartulid" }
print(ostukorv)

# kasutame set() funktsiooni stringi peal
a = set("abracadabra")
print(a)

# Hulga elementide arvu teada saamine
print(len(a))

# Tehted ulkade peal
b = set('alacazam')
print(b)

print(a - b)  # a elemendid, mida b-s ei leidu (vahe)
print(a | b)  # Elemendid, mis on a-s, b-s või mõlemas (ühend)
print(a & b)  # Elemendid, mis on nii a-s, kui b-s (ühisosa)
print(a ^ b)  # Elemendid, mis on a-s või b-s, kuid mitte mõlemas (välistav või)


# Elementide läbi jooksmine
for toode in ostukorv:
	print(toode)

# Eemaldame listist elemendi - annab vea
del list[2]

#
# Operatsioonid listide peal
#

# Listide korrutamine
print(tup*4)

# min(), max() ja sum() funktsioonid
tup2 = (12, 82, 32, 77, 52, 49)
print(min(tup2))
print(max(tup2))
print(sum(tup2))


# Sorteerimine
print(sorted(tup2))


# Tuple muutuja eemaldamine
del tup
