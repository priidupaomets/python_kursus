"""
veahaldus.py

Vigade haldamine
"""

#
# Vigade haldamine 
#

# Võtame viimased funktsioonid ja vaatame, kuidas me saaks oma koodi veakindlamaks muuta
def numsum(*numbrid):
    sum = 0
    for num in numbrid:
        if isinstance(num, int) or isinstance(num, float):
            sum += num
    return sum

def numcount(*numbrid):
    count = 0
    for num in numbrid:
        if isinstance(num, int) or isinstance(num, float):
            count += 1
    return count

def numavg(*numbrid):
    sum = numsum(*numbrid)
    count = numcount(*numbrid)
    result = 0.0

    try:
        result = sum / (count * 1.0)
    except ZeroDivisionError as err:
        print("0-jagamise viga:", err)
        result = 0.0
    except:
        print("Mingi muu viga")
        raise      # Kutsume sama vea uuesti välja
    else:
        print(f"Tulemus on {result}")
    finally:
        print("finally")
        return result

print(numavg(1))
print("-"*30)    
print(numavg())             

# Vigade välja kutsumine
raise ValueError('Esimese argumendi väärtus peab olema vahemikus 1..50')
raise IOError('file error')


#
# with-avaldis 
#

# Tavaline kaitsmata vorm faili kasutusest, ressursid vabastatakse kunagi hiljem
for rida in open('minufail.txt'):
    print(rida, end = "")

# Natuke parem vorm, kus me teadlikult sulgeme faili 
f = open('minufail.txt')

for rida in f:
    print(rida, end = "")

f.close()

# try-finally poolt kaitstud vorm, kuid ei kata faili avamisel tekkivaid vigu
f = open('minufail.txt')
try:
    for rida in f:
        print(rida, end = "")
finally:
    f.close()


# Kaitstud vorm ja lisaks vabastab ressursid kohe kui lõpetab
with open('minufail.txt') as f:
    for rida in f:
        print(rida, end = "")