"""
dictionary.py

Sõnastike olemus, deklareerimine ja kasutamine
"""

#
# Sõnastiku vajaduse selgitamine
#

#Inimesed ja nende vanused
isikud = [ "Mati", 23, "Karl", 20, "Triin", 28 ]
print(iskikud)

# Sõnastik
inimesed = { "Mati": 23, "Karl": 20, "Triin": 28 }
print(inimesed)

#
# Sõnastiku deklareerimine
#

# Tühja sõnastiku deklareerimine
dict = {}
print(dict)


# Pöördume individuaalsete elementide poole
# ... indeks annab vea
print(inimesed[0])
# ... võtme järgi töötab
print(inimesed["Mati"])
# ... kuna võti on tõstutundlik, siis väiketähega varianti ei leita
print(inimesed["mati"])


# Kui palju elemente listis üldse on
print(len(inimesed))

# Individuaalse väärtuse muutmine
inimesed["Mati"] = 24
print(inimesed)

# uue väärtuse lisamine
inimesed["Kati"] = 19
print(inimesed)

# Eemaldame listist elemendi
del list["Karl"]

# Võtmete teada saamine
print(inimesed.keys)

# Väärtuste teada saamine
print(inimesed.values())

# Ühele sõnastikule teise lisamine
tudengid = { "Meelis": 20, "Jörgen": 31 }
inimesed.update(tudengid)
print(inimesed)

# sõnastiku tühjendamine
inimesed.clear()
print(inimesed)
