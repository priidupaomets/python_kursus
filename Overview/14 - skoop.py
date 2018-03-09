"""
skoop.py

Muutujate ja funktsioonide nähtavuse reeglid
"""

#
# Globaalse muutuja kasutamine funktsioonis ja välaspool seda
#

a = 0

def func():
    print("Sisemine:", a)

func()
print("Välimine:", a)

#
# Samanimelise muutuja kasutamine funktsioonis ja välaspool seda
#

a = 0

def func2():
    a = 11
    print("Sisemine:", a)

func2()
print("Välimine:", a)

#
# Funktsiooni sees globaalse muutuja kasutamine ja selle muutmine
#

a = 0

def func3():
    global a 
    a = 11
    print("Sisemine:", a)

func3()
print("Välimine:", a)

#
# Mitmetasemelised näited
#

# Kohalikud muutujad
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 1
# global: 0

# Mitte-lokaalsed muutujad
x = 0
def outer2():
    x = 1
    def inner2():
        nonlocal x
        x = 2
        print("inner:", x)

    inner2()
    print("outer:", x)

outer2()
print("global:", x)

# inner: 2
# outer: 2
# global: 0

# Globaalsed muutujad
x = 0
def outer3():
    x = 1
    def inner3():
        global x
        x = 2
        print("inner:", x)

    inner3()
    print("outer:", x)

outer3()
print("global:", x)

# inner: 2
# outer: 1
# global: 2

