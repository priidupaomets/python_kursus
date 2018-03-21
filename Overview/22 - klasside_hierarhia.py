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
