"""
funktsioonid.py

Funktsioonide ja protseduuride kasutamine
"""

#
# Protseduur
#
def minu_funktsioon():
    print("See on protseduur")

# Kutsume funktsiooni välja
minu_funktsioon()


#
# Funktsioon
#
def liida(num1, num2):
    return num1 + num2

sum = liida(3, 5)
print(sum)

# Näide vaikeväärtuste kasutamisest
# def funk(arg1 = väärtus1, arg2 = väärtus2)
#    pass

def funk(arg1 = 0, arg2 = "Test"):
    print(arg1, arg2)

funk() # Kutsume funktsiooni välja ilma argumente kaasa andmata

#
# Algarvude leidmine
#
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

# Kustume funktsiooni testimiseks välja
n = 5
if isprime(n):
    print(f"{n} ON algarv")  # Kasutame f-formaatimisstringi, mis lubab muutuja otse stringi sisse panna
else:
    print(f"{n} EI OLE algarv")


def list_primes(max_num = 100):
    for n in range(2, max_num):
        if isprime(n):
            print(n, end = ' ', flush = True)
    print()

list_primes()


#
# Muutuva arvu argumentidega funktsioonid
#

# Lisame lihtsalt uusi argumente
def summa(num1, num2, num3):
    return num1 + num2 + num3

print(summa(1, 2, 3))  # Töötab
print(summa(1, 2))     # Saame vea, kuna uus funktsioon nõuab 3 argumenti


# Katsetame funktsiooni ülelaadimist (function overloading või method overloading)
def summa(num1, num2):
    return num1 + num2

def summa(num1, num2, num3):
    return num1 + num2 + num3

print(summa(1, 2))     # Saame vea, kuna viimane def kirjutab eelmise üle
print(summa(1, 2, 3))

# Katsetame vaikeväärtustega funktsioone
def summa(num1, num2, num3 = 0, num4 = 0):
    return num1 + num2 + num3 + num4

print(summa(1, 2))     
print(summa(1, 2, 3))
print(summa(1, 2, 3, 4))
#print(summa(1, 2, 3, 4, 5)) # Selle tööle saamiseks peame f-ni muutma

def keskmine(num1, num2, num3 = 0, num4 = 0):
    sum = num1 + num2 + num3 + num4   # Sama, mis summa(num1, num2, num3, num4)
    argumente = 4.0
    return sum / argumente

print(keskmine(1, 2))       # Ilmselgelt vale tulemus (1.5 asemel 0.75)     
print(keskmine(1, 2, 3))    # Ka vale tulemus (2 asemel 1.5)
print(keskmine(1, 2, 3, 4)) # Õige tulemus

# Täiendame argumentide arvu leidmist
def keskmine(num1, num2, num3 = 0, num4 = 0):
    sum = num1 + num2 + num3 + num4   # Sama, mis summa(num1, num2, num3, num4)
    argumente = 2.0         # Minimaalselt 2
    if num3 > 0:
        argumente = argumente + 1
    if num4 > 0:
        argumente = argumente + 1
    return sum / argumente

print(keskmine(1, 2))       # Õige tulemus  
print(keskmine(1, 2, 3))    # Õige tulemus
print(keskmine(1, 2, 3, 4)) # Õige tulemus 
print(keskmine(1, 2, 3, 0)) # Vale tulemus! 
print(keskmine(1, 0, 3, 2)) # Õige tulemus!?! Kuidas see nüüd õige on - kas tulemus sõltub argumentide järjekorrast?

# Kasutame teistsugust vaikeväärtust
def keskmine(num1, num2, num3 = None, num4 = None):
    sum = num1 + num2       # Ei saa kohe 4 arg'i kokku liita
    argumente = 2.0         # Minimaalselt 2
    if num3 is not None:
        argumente += 1
        sum = sum + num3
    if num4 is not None:
        argumente += 1
        sum = sum + num4
    return sum / argumente

print(keskmine(1, 2))       # Õige tulemus  
print(keskmine(1, 2, 3))    # Õige tulemus
print(keskmine(1, 2, 3, 4)) # Õige tulemus 
print(keskmine(1, 2, 3, 0)) # Õige tulemus! 
print(keskmine(1, 0, 3, 2)) # Õige tulemus

# Proovime listiga argumente defineerida
def summa(numbrid=[]):
    sum = 0
    for num in numbrid:
        sum += num
    return sum

#print(summa(1))             # Ei tööta, kuna pole itereeritav tüüp
#print(summa(1, 2))          # Ei tööta, kuna pole massiiv

arvud=[1, 2]
print(summa(arvud))
arvud=[1, 2, 3]
print(summa(arvud))
arvud=[1, 2, 3, 4]
print(summa(arvud))

print(summa([1, 2, 3, 4, 5])) # Võime panna ka ilma vahemuutujata
arvud=[1]
print(summa(arvud))


def summa(*numbrid):
    sum = 0
    for num in numbrid:
        sum += num
    return sum

print(summa())               # Isegi see variant töötab
print(summa(1))
print(summa(1, 2))

arvud=[1, 2]
print(summa(*arvud))         # Ka siin tuleb '*' kasutada
arvud=[1, 2, 3]
print(summa(*arvud))
arvud=[1, 2, 3, 4]
print(summa(*arvud))
arvud=[1, 2, 3, 4, 5]
print(summa(*arvud))
arvud=[1]
print(summa(*arvud))

# Erinevat sort argumendid
def argfun(arg1, arg2, *args, kw1 = 1, kw2 = "True"):
    print(arg1, arg2, *args, kw1, kw2)

argfun(1, 2, 3, 4, 5, kw1 = 10, kw2 = 12)

def argfun(**kwargs):
    for (arg, val) in kwargs.items():
        print(f"{arg}={val}", end = ' ')
    print()

argfun(kw2 = 10, kw3 = 12, kw4 = 14)


def argfun(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args)

    for (arg, val) in kwargs.items():
        print(f"{arg}={val}", end = ' ')
    print()

argfun(1, 2, 3, 4, 5, kw2 = 10, kw3 = 12, kw4 = 14)

def argfun(arg1, arg2, *args, kw1 = 1, kw2 = "True", **kwargs):
    print(arg1, arg2, *args, kw1, kw2)
    
    for (arg, val) in kwargs.items():
        print(f"{arg}={val}", end = ' ')
    print()

argfun(1, 2, 3, 4, 5, kw2 = 10, kw3 = 12, kw4 = 14)

# Kuidas garanteerida, et argumentideks on numbrid?
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

    return sum / (count * 1.0) # Võime jagatava teha float tüübiks


print(numsum(1))             
print(numsum(1, 2))          
print(numsum(1, 2, 3))
print(numsum(1, 2, 3, "4"))
print(numsum(1, None, 3, 4, 5))    
print("-"*30)

print(numcount(1))             
print(numcount(1, 2))         
print(numcount(1, 2, 3))
print(numcount(1, 2, 3, "4"))
print(numcount(1, None, 3, 4, 5))    
print("-"*30)

print(numavg(1))             
print(numavg(1, 2))          
print(numavg(1, 2, 3))
print(numavg(1, 2, 3, "4"))
print(numavg(1, None, 3, 4, 5))    

print(numavg())             # Viga! Nulliga jagamine!!!

# Vigade haldamist vaatame peatselt ka lähemalt
