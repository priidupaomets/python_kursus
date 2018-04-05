"""
omadused.py

Lisavõimalus klassi funktsionaalsuse laiendamiseks
"""
#
# Tavaline klass, milles on muutuja
#

class Aeg:
    def __init__(self):
        self.praegu = 0


aeg = Aeg()
print(aeg.praegu)  # Ei anna mingit mõistlikku tulemust, kuna ei omistata!
print(aeg.praegu)  # Ei anna mingit mõistlikku tulemust, kuna ei omistata!

print("-"*30)

#
# Tavaline klass
#

import time

class MuutuvAeg:
    def get_praegu(self):
        return time.localtime()


aeg = MuutuvAeg()
print(aeg.get_praegu())
time.sleep(1)
print(aeg.get_praegu())

print("-"*30)

#
# Defineerime omaduse
#

import time

class OmadusegaAeg:
    @property
    def praegu(self):
        return time.localtime()


aeg = OmadusegaAeg()
print(aeg.praegu)
time.sleep(1)
print(aeg.praegu)

print("-"*30)

class OmadusegaAegEx:
    def __init__(self):
        self._now = None

    def __update(self):
        self._now = time.localtime()

    @property
    def praegu(self):
        return self._now

    @praegu.setter
    def praegu(self, value):
        self._now = value

    @praegu.deleter
    def praegu(self):
        del self._now

# Alternatiivne variant
class OmadusegaAegEx2:
    def __init__(self):
        self._now = None

    def __update(self):
        self._now = time.localtime()

    def getpraegu(self):
        return self._now

    def setpraegu(self, value):
        self._now = value

    def delpraegu(self):
        del self._now

    praegu = property(getpraegu, setpraegu, delpraegu, "Mina olen kellaaja omadus")
