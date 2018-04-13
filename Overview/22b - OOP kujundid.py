from abc import ABCMeta, abstractmethod

class Kujund(metaclass = ABCMeta):
    @abstractmethod
    def tutvusta(self):
        print("Ma ei tea, kes ma olen")

class Ruut(Kujund):
    def tutvusta(self):
        #super.tutvusta()
        print("Ruut")

class Ring(Kujund):
    def tutvusta(self):
        print("Ring")

class Kolmnurk(Kujund):
    def tutvusta(self):
        print("Kolmnurk")

def tutvusta(*kujundid):
    for kujund in kujundid:
        kujund.tutvusta()

list = (Kolmnurk(), Ruut(), Ring())

tutvusta(*list)
