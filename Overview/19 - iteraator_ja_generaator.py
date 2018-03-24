"""
iteraator_ja_generaator.py

Iteraatorite ja generaatorite näited
"""

#
# Iteraator
#

d1 = [1, 2, 3, 4, 5]
iteraator = iter(d1)
print(next(iteraator)) # 1
print(next(iteraator)) # 2
print(next(iteraator)) # 3
print(next(iteraator)) # 4
print(next(iteraator)) # 5
print(next(iteraator)) # põhjustab StopIteration vea, mis lõpetab edasi mineku


#
# Generaator
#
(i*i for i in range(10))

print((i*i for i in range(10)))

print(sum(i*i for i in range(10)))


# generaatori loomine ja selle samm-haaval läbimine
mygenerator = (taht for taht in 'abcdefg')
print(next(mygenerator)) # a
print(next(mygenerator)) # b
print(next(mygenerator)) # c
print(next(mygenerator)) # d
print(next(mygenerator)) # e
print(next(mygenerator)) # f
print(next(mygenerator)) # g
print(next(mygenerator)) # StopIteration viga, mis lõpetab edasi mineku


# Tavaline funktsioon andmehulga tagurpidi keeramiseks
def reverse(data):
    reversedData = []
    for index in range(len(data)-1, -1, -1):
        reversedData.append(data[index])
    return reversedData

# Loome listi algandmetega
d1 = [1, 2, 3, 4, 5]
d2 = reverse(d1)
print(d2) 

#Jookseme listi läbi
for item in d2:
    print(item)

# Sama asi generaator-iteraator funktsiooni abil, kasutades yield-võtmesõna
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

# Loome listi algandmetega
d1 = [1, 2, 3, 4, 5]
d2 = reverse(d1)
print(d2)       # Annab meile listi asemel hoopis "<generator object reverse at 0x000001340B77E4C0>"
print(list(d2)) # See töötab

# Itereerime generaatori iteraatori
for item in d2:
    print(item)


