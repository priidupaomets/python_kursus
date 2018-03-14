"""
list_comprehensions.py

Vaatama listide hõlmamise/haldamise võimalusi
"""

# Kõik paaritud arvud vahemikus 1..10
minu_list = [elem for elem in range(1, 10, 2)]
print(minu_list)

# Sarnane eelmisele, kuid trükime välja individuaalsed elemendid 
[print(elem, end=' ') for elem in range(1, 10, 2)]

# Sama asi, kuid veidi teistmoodi kirjutatuna
minu_list = [elem for elem in range(1, 10) if elem % 2 != 0]
print(minu_list)

# Arvud vahemikus 0..99, mis jaguvad nii kolme kui viiega
minu_list = [elem for elem in range(0, 99, 3) if elem % 3 == 0 and elem % 5 == 0]
print(minu_list)

# Arvude ruutude arvutamine
arvude_ruudud = [x**2 for x in range(10)]
print(arvude_ruudud)

# Arvude ruudud lambda-avaldise kujul
arvude_ruudud = list(map(lambda x: x**2, range(10)))
print(arvude_ruudud)

# listide unikaalsete väärtuste kombineerimine
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

# Sama asi teisel kujul
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

# zip funktsiooni kasutamine
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
zipped = zip(list1, list2)
print(list(zipped))
# [(1, 6), (2, 7), (3, 8), (4, 9)]

list3 = [10, 11, 12, 13]
zipped = zip(list1, list2, list3)
print(list(zipped))
# [(1, 6, 10), (2, 7, 11), (3, 8, 12), (4, 9, 13)]


# Maatriksi transponeerimine
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
 
transpose = [[row[n] for row in matrix] for n in range(4)]
 
print(transpose)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# Numbrite (1..10) ja nende ruutude ning kuupide genereerimine ja formateerimine
[print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x)) for x in range(1, 11)]
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000