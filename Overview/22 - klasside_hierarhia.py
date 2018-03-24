"""
klasside_hierarhia.py

Objekt-orienteeritud programmeerimise klasside hierarhia ja põlvnemine
"""
#
# Lihtne klasside hierarhia
#

class Eellane:
    def __init__(self):
        print("See on eellane")

    def eellaseFunktsioon(self):
        print("Eellase funktsioon")

class Järglane(Eellane):      # Lisame sulgudes eellasklassi nime
    def __init__(self):
        print("See on järglane")

    def järglaseFunktsioon(self):
        print("Järglase funktsioon")

eellane = Eellane()
eellane.eellaseFunktsioon()

järglane = Järglane()
järglane.järglaseFunktsioon()
järglane.eellaseFunktsioon()  # Eellaselt päritud meetod


#
# Klasside sügavam hierarhia
#

class Loom:
    def häälitse(self):
        pass

class Koer(Loom):
    def haugu(self):
        pass

class Kass(Loom):
    def nurru(self):
        pass

class Hobune(Loom):
    def hirnu(self):
        pass

    def traavi(self):
        pass

class Lõvi(Loom):
    def möirga(self):
        pass

class SomaaliaKass(Kass):
    pass

class PärsiaKass(Kass):
    pass

class SiiamiKass(Kass):
    pass


#
# Mitmik-põlvnemine (multiple inheritance)
#

class Operatsioonisüsteem:
    multitegumiline = True
    nimi = "MacOSX"

class Apple:
    nimi = "Apple"
    veebisait = "www.apple.com"

class MacBook (Operatsioonisüsteem, Apple):
    def __init__(self):
        if self.multitegumiline is True:
            print("See on multi-taskiv süsteem.", end=' ')
            print(f"Rohkema info saamiseks külasta {self.veebisait}")
        print(f"Nimi: {self.nimi}")       # Kumb nimi siia tuleb?

arvuti = MacBook()

#
# Rombikujulise põlvnemise probleem (Diamon Shape Problem)
#

# Variant 1: Ükski klass ei kirjuta meetodit üle
class A:
    def method(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.method()  # Tulemus: A

# Variant 2: Klass A kirjutab meetodi üle
class A1:
    def method(self):
        print("A")

class B1(A1):
    def method(self):
        print("B")

class C1(A1):
    pass

class D1(B1, C1):
    pass

d = D1()
d.method()  # Tulemus: B

# Variant 3: Klass B kirjutab meetodi üle
class A2:
    def method(self):
        print("A")

class B2(A2):
    pass

class C2(A2):
    def method(self):
        print("C")

class D2(B2, C2):
    pass

d = D2()
d.method()  # Tulemus: C

# Variant 4: Nii klass B, kui ka C kirjutavad meetodi üle
class A3:
    def method(self):
        print("A")

class B3(A3):
    def method(self):
        print("B")

class C3(A3):
    def method(self):
        print("C")

class D3(B3, C3):
    pass

d = D3()
d.method()  # Tulemus: B


#
# Protected liikmete kaitsmise tase
#

class Juur:
    _sisemine = 0
    def __init__(self):
        self._sisemine = "Klassi hierarhia"

class Oks(Juur):
    def test(self):
        print(f"{self._sisemine}")


obj = Oks()
obj.test()  # Tulemus: "Klassi hierarhia"
obj._sisemine = 12
obj.test()  # Tulemus: 12

# Seega saame protected liikmetele ikka ligi, kuid vihjab teistele, et see pole mõeldud üldiseks kasutamiseks
