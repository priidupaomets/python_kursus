"""
lambda.py

Lambda avaldised ja funktsioonid
"""

# Traditsiooniline ruutu võtmise funktsioon
def double(x):
    return x * 2
print(double(5), type(double))

# Lambda-funktsiooni loomine
double = lambda x: x * 2        # Omistame muutujale funktsiooni (mitte väärtuse!)
print(double(5), type(double))  # Kutsume funktsiooni muutuja kaudu välja

# Listi filtreerimine, tuues välja vaid paaris arvud
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)    # Output: [4, 6, 8, 12]

# Ruutude arvutamine
ruudud = list(map(lambda x: x**2, range(10)))
print(ruudud)


# Näide funktsioonist, mis tagastab teise funktsiooni (hetkel lambda-avaldise kujul)
def loo_suurendaja(n):
    return lambda x: x + n

inc = loo_suurendaja(42)
inc(0)  # tulemuseks 42
int(1)  # tulemuseks 43

# Sorteerime listi 
paarid = [(1, "Üks"), (2, "Kaks"), (3, "Kolm"), (4, "Neli")]
paarid.sort(key = lambda paar: paar[1])  # Sorteerime nime järgi
print(paarid)
