"""
listid.py

Listide olemus, deklareerimine ja kasutamine
"""

#
# Listi deklareerimine
#

# Tühja listi deklareerimine
list = []
print(list)

# list, milles on mõned elemendid
list = ["Tekst", 35, 12.5, True]
print(list)

# Pöördume individuaalsete elementide poole
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# Kui palju elemente listis üldse on
print(len(list))

# Individuaalse väärtuse muutmine
list[1] = 46
print(list)

# Uue väärtuse lisamine listi (append() ja insert())
# ... lisame listi lõppu
list.append(18)
# ... pistame listi keskele
list.insert(2, "Uus tekst")
print(list)

# Eemaldame listist elemendi
del list[2]

#
# Operatsioonid listide peal
#

# Listide liitmine
list2 = [18, 20.5, 99]
list3 = list + list2
print(list3)

# min() ja max() funktsioonid
print(min(list2))
print(max(list2))

# see annab meile vea, kuna seal on lisks numbritele ka tekst ja tõeväärtus
print(min(list))

# count(), mis tagastab küsitud väärtuse esinemmise arvu
print(list.count(18))

# listi tühjendamine
list.clear()
print(list)

#
# Sorteerimine
#
list = [17, 99, 1]

# Kasutame sorted() funktsiooni, mis tagastab uue listi sorteeritud kujul
print(sorted(list))
# Vaatame, mis originaalist sai - kõik on vanaviisi
print(list)
# Kasutame sort() funktsioone
list.sort()
# Vaatame originaallisti sisu - nüüd on see sorteeritud
print(list)
