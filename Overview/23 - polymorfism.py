"""
polymorfism.py

Objekt-orienteeritud programmeerimise polümorfism
"""
#
# Lihtne polümorfirmi näide
#

class Eellane:
    def __init__(self, nimi):
        self.nimi = nimi

    def eellaseFunktsioon(self):
        print("Eellase funktsioon")

class Järglane(Eellane):      
    def __init__(self, nimi):
        super().__init__(nimi)    # Kutsume välja eellasklassi konstruktori

    def järglaseFunktsioon(self):
        print("Järglase funktsioon")

def töötle(obj: Eellane):
    print(f"{obj.nimi}")
    obj.eellaseFunktsioon()

obj1 = Eellane("Eellane")
obj2 = Järglane("Järglane")

töötle(obj1)
töötle(obj2)

print("-"*30)

#
# Sama asi meetodi üle kirjutamisega
#

class Eellane2:
    def __init__(self, nimi):
        self.nimi = nimi

    def trüki(self):
        print("Eellase funktsioon")

class Järglane2(Eellane2):      
    def __init__(self, nimi):
        super().__init__(nimi)    # Kutsume välja eellasklassi konstruktori

    def trüki(self):
        #super().trüki()          # Soovi korral saaks välja kutsuda ka eelase oma
        print("Järglase funktsioon")

def töötle2(obj: Eellane):
    print(f"{obj.nimi}")
    obj.trüki()

obj1 = Eellane2("Eellane")
obj2 = Järglane2("Järglane")

töötle2(obj1)
töötle2(obj2)

print("-"*30)

#
# Klasside sügavam hierarhia koos polümorfismiga
#

class Loom:
    def häälitse(self):
        pass

class Koer(Loom):
    def häälitse(self):
        self.haugu()

    def haugu(self):
        print("Haugu")

class Kass(Loom):
    def häälitse(self):
        self.nurru()
        
    def nurru(self):
        print("Nurru")

class Hobune(Loom):
    def häälitse(self):
        print("Hirnu")
        
class Lõvi(Loom):
    def häälitse(self):
        print("Möirga")


print("-"*30)

#
# Klasside sügavam hierarhia koos abstraktse klassiga
#

from abc import ABCMeta, abstractmethod

class Loom2(metaclass = ABCMeta):
    @abstractmethod
    def häälitse(self):
        pass

class Koer2(Loom2):
    def häälitse(self):
        self.haugu()

    def haugu(self):
        print("Haugu")

class Kass2(Loom2):
    def häälitse(self):
        self.nurru()
        
    def nurru(self):
        print("Nurru")

class Hobune2(Loom2):
    def häälitse(self):
        print("Hirnu")
        
class Lõvi2(Loom2):
    pass
#    def häälitse(self):
#        print("Möirga")


# loom = Loom2()
# kass = Kass2()
# lõvi = Lõvi2()

# loom.häälitse()
# kass.häälitse()
# lõvi.häälitse()

print("-"*30)

#
# Duck typing näide
#

class Papagoi:
    def lenda(self):
        print("Papagoi lendab")

class Lennuk:
    def lenda(self):
        print("Lennuk lendab")

class Vaal:
    def uju(self):
        print("Vaal ujub")

def tõuse_lendu(entity):
    entity.lenda()

papagoi = Papagoi()
lennuk = Lennuk()
vaal = Vaal()

tõuse_lendu(papagoi) # Trükib 'Papagoi lendab'
tõuse_lendu(lennuk)  # Trükib 'Lennuk lendab'
tõuse_lendu(vaal)    # Viga: `'Vaal' object has no attribute 'lenda'`



