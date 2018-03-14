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
#import datetime

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
            print(f"{self.nimi}: Eesmärk on saavutatud")
        else:
            print(f"{self.nimi}: Eesmärgist jäi puudu {5 - self.nädalaMüük}")

madis = Töötaja("Madis", "Müügijuht", 25)
madis.kasNädalaMüüginormOnTäidetud()

karl = Töötaja("Karl", "Müügiagent", 20)
karl.nädalaMüük = 7
karl.kasNädalaMüüginormOnTäidetud()