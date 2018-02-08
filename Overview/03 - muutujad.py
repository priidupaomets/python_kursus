"""
muutujad.py

Muutujate deklareerimine ja kasutamine, andmetüübid ja aritmeetilised operatsioonid
"""

# Lihtsam muutujate omistamised ja kasutamised
a = 3 + 5
b = (12 + 8) * 12 / 6
print(a) # Väljund: 8
print(b) # Väljund: 40.0

c = a + b
print(c) # Väljund: 48.0


# Muutujatele saab uusi väärtusi omistada, isegi kui need on teist tüüpi
a = "Tere"
print(a)  # Väljund: Tere


# Mitme muutuja samaaegne omistamine
a = b = c = 12.6
print(a) # Väljund: 12.6
print(b) # Väljund: 12.6
print(c) # Väljund: 12.6


# Mitme muutuja üheaegne omistamine, kui neile tuleb anda erinevad väärtused
a, b, c, d = 1, 5.7, "Tere", True
print(a) # Väljund: 1
print(b) # Väljund: 5.7
print(c) # Väljund: 'Tere'
print(d) # Väljund: True


# Eelnevas me nägime erinevate andmetüüpide kasutust - numbrid, tekst ja tõeväärtus
# Numbrid võivad olla kas täisarvud...
print(5)
# ... või reaalarvud
print(2.1)
# Tekst kirjutatakse jutumärkide vahele...
print("Tere")
# ... või ülakomade vahele
print('Tere')
# Tõeväärtusi on kaks tükki: tõene (True) ja väär (False)
print(True)
print(False)


# Enamus andmetüüpe toetavad üht või enamat operatsiooni, kuigi nende semantika
# võib olla pisut erinev. Numbriliste andmete puhul on meil võimalik kasutada
# järgmisi aritmeetilisi operatsioone:

# Liitmine
print(3 + 2) # Väljund: 5

# Lahutamine
print(17 - 3) # Väljund: 14

# Korrutamine
print(3 * 6) # Väljund: 18

# Jagamine
print(5 / 2) # Väljund: 2.5

# Moodul ehk jääk
print(5 % 2) # Väljund: 1

# Astendamine
print(2 ** 3) # Väljund: 8

# Allapoole ümardatud jagamine
print(5 // 2) # Väljund: 2
