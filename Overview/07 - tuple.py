"""
tuple.py

Tuple olemus, deklareerimine ja kasutamine
"""

#
# Deklareerimine
#

# Tühja tuple deklareerimine
tup = ()
print(tup)

# tuple, milles on mõned elemendid
tup = ("Tekst", 35, 12.5, True)
print(tup)

# Pöördume individuaalsete elementide poole
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

# Kui palju elemente listis üldse on
print(len(tup))

# Individuaalse väärtuse muutmine - annab vea
tup[1] = 46
print(tup)

# Uue väärtuse lisamine listi - annab vea
list.append(18)

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
