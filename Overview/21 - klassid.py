"""
klassid.py

Objekt-orienteeritud programmeerimise baasitõed
"""
#
# Lihtne klass ja selle kasutamine
#

class Koer:
    värvus = ""

    def haugu(self):
        print(f"Auhh, ütles {self.värvus} koer")

pontu = Koer()
pontu.värvus = "Must, Pruun"
pontu.haugu()

#
# Klass koos värvi seadmise meetodiga
#

class Koer:
    värvus = ""

    def algväärtusta(self, värvus):
        self.värvus = värvus

    def haugu(self):
        print(f"Auhh, ütles {self.värvus} koer")

pontu = Koer()
pontu.algväärtusta("Must")
pontu.haugu()


#
# Klass koos konstruktoriga
#

class Koer:
    värvus = ""

    def __init__(self, värvus):
        self.värvus = värvus

    def haugu(self):
        print(f"Auhh, ütles {self.värvus} koer")

pontu = Koer("Must")
pontu.haugu()


#
# Pisut sisukam klass
#

class Töötaja:
    nimi = ""
    amet = ""
    vanus = None
    nädalaMüük = 0

    def __init__(self, nimi, amet, vanus):
        self.nimi = nimi
        self.amet = amet
        self.vanus = vanus

    def kasNädalaMüüginormOnTäidetud(self):
        if self.nädalaMüük >= 5:
            print(f"{self.nimi}: Eesmärk on saavutatud ({self.nädalaMüük})")
        else:
            print(f"{self.nimi}: Eesmärgist 5 jäi puudu {5 - self.nädalaMüük}")

madis = Töötaja("Madis", "Müügijuht", 25)
madis.kasNädalaMüüginormOnTäidetud()

karl = Töötaja("Karl", "Müügiagent", 20)
karl.nädalaMüük = 7
karl.kasNädalaMüüginormOnTäidetud()


#
# Konstruktor, kus lisatakse isendi-taseme muutuja
#

class Töötaja:
    nimi = ""
    amet = ""
    vanus = None
    nädalaMüük = 0

    def __init__(self, nimi, amet, vanus):
        self.nimi = nimi
        self.amet = amet
        self.vanus = vanus
        self.sisemine = 12    # Objekti-tasandil muutuja, mis luuakse meetodi sees

    def kasNädalaMüüginormOnTäidetud(self):
        print(f"{self.nimi}: Sisemine muutuja: {self.sisemine}")
        if self.nädalaMüük >= 5:
            print(f"{self.nimi}: Eesmärk on saavutatud ({self.nädalaMüük})")
        else:
            print(f"{self.nimi}: Eesmärgist 5 jäi puudu {5 - self.nädalaMüük}")

Töötaja.nädalaMüük = 30  # Omistame klassi tasemel muutujale / atribuudile vaikeväärtuse ja see kehtib kõigile

madis = Töötaja("Madis", "Müügijuht", 25)
madis.kasNädalaMüüginormOnTäidetud()

karl = Töötaja("Karl", "Müügiagent", 20)
karl.nädalaMüük = 7
karl.kasNädalaMüüginormOnTäidetud()
karl.sisemine      # Sellele sisemisele muutujale saame ligi ka väljastpoolt

# Tänu dünaamilisusele, võime üksikutele isenditele veel eraldi muutujaid/atribuute lisada
madis.palk = 2000
print(f"Madise palk on {madis.palk}")
#print(f"Karli palk on {karl.palk}")    # Saame vea

#
# Äärmuslik klassi loomise näida
#

class Töötaja:             # Loome tühja klassi kesta
    pass

jaan = Töötaja()           # Loome objekti

jaan.nimi = "Jaan Keegi"   # Loome kirje väljad ja omistame väärtused
jaan.osakond = "Müük"
jaan.palk = 1950


#
# Avalikud ja privaatsed andmed
#

class Loendur:
    __eksemplarideArv = 0   # Privaatne klassi tasemel atribuut

    def __init__(self):
        Loendur.__eksemplarideArv += 1

    def trükiSeis(self):
        print(f"Eksemplare: {self.__eksemplarideArv}")

loendur1 = Loendur()
loendur1.trükiSeis()

loendur2 = Loendur()
loendur2.trükiSeis()

#print(loendur1.__eksemplarideArv)          # Saame vea
print(loendur1._Loendur__eksemplarideArv)  # Tegelikult nimetatakse sisemiselt ümber

# Loendur.trükiSeis(loendur1)

#
# Staatiline meetod
#

class Tervitus:
    @staticmethod
    def tervita():
        print("Tere tulemast")

t = Tervitus()
t.tervita()

Tervitus.tervita()

