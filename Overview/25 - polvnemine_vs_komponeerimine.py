"""
polvnemine_vs_komponeerimine.py

Klasside põlvnemise ja komponeerimise võrdlus 
"""
#
# Liidese-laadsed asjad Pythoni abstraktsete klasside kaudu
#
from abc import ABCMeta, abstractmethod

class ILoom(metaclass = ABCMeta):
    vanus = 0

    @abstractmethod
    def söö(self):
        pass

    @abstractmethod
    def maga(self):
        pass

class IKõndiv(metaclass = ABCMeta):
    @abstractmethod
    def kõnni(self):
        pass


#
# Põlvnemine baas-klassidest
#
class Inimene(ILoom, IKõndiv):
    def söö(self):
        pass
    def maga(self):
        pass
    def kõnni(self):
        pass

class Koer(ILoom, IKõndiv):
    def söö(self):
        pass
    def maga(self):
        pass
    def kõnni(self):
        pass

class Kuldkala(ILoom):
    def söö(self):
        pass
    def maga(self):
        pass


#
# Kompositsiooni näide
#

# Esimene katsetus otsest abstraktset baasklassi kasutades
class InimeneComp():
    def __init__(self):
        self.__loom = ILoom()
        self.__kõndiv = IKõndiv()

    def söö(self):
        self.__loom.söö()

    def maga(self):
        self.__loom.maga()

    def kõnni(self):
        self.__kõndiv.kõnni()


# Teine variant, kus loome konkreetsed klassid
class Loom(ILoom):
    def söö(self):
        print("söö")   

    def maga(self):
        print("maga")   

class Kõndiv(IKõndiv):
    def kõnni(self):
        print("kõnni")   


# Abstraktse klassi asemel kasutame nüüd konkreetset klassi
class InimeneComp2():
    def __init__(self):
        self.__loom = Loom()
        self.__kõndiv = Kõndiv()

    def söö(self):
        self.__loom.söö()

    def maga(self):
        self.__loom.maga()

    def kõnni(self):
        self.__kõndiv.kõnni()

inimene = InimeneComp2()
inimene.söö()
inimene.maga()
inimene.kõnni()

print("-"*30)

# Nüüd muudame kompositsiooni implementatsiooni kohandatavaks
class InimeneComp3():
    def __init__(self, loom : ILoom, kõndiv: IKõndiv):
        self.__loom = loom
        self.__kõndiv = kõndiv
    def söö(self):
        self.__loom.söö()
    def maga(self):
        self.__loom.maga()
    def kõnni(self):
        self.__kõndiv.kõnni()

class KoerComp:
    def __init__(self, loom : ILoom, kõndiv: IKõndiv):
        self.__loom = loom
        self.__kõndiv = kõndiv
    def söö(self):
        self.__loom.söö()
    def maga(self):
        self.__loom.maga()
    def kõnni(self):
        self.__kõndiv.kõnni()



class IUjuv(metaclass = ABCMeta):
    @abstractmethod
    def uju(self):
        pass

class KuldkalaComp:
    def __init__(self, loom : ILoom, ujuv: IUjuv):
        self.__loom = loom
        self.__ujuv = ujuv
    def söö(self):
        self.__loom.söö()
    def maga(self):
        self.__loom.maga()
    def uju(self):
        self.__ujuv.uju()


class PartComp:
    def __init__(self, loom : ILoom, kõndiv: IKõndiv, ujuv: IUjuv):
        self.__loom = loom
        self.__kõndiv = kõndiv
        self.__ujuv = ujuv
    def söö(self):
        self.__loom.söö()
    def maga(self):
        self.__loom.maga()
    def kõnni(self):
        self.__kõndiv.kõnni()
    def uju(self):
        self.__ujuv.uju()
        

# Konkreetsete klasside kasutamine teiste sees



class Ujuv(IUjuv):
    def uju(self):
        print("uju")    


loom = Loom()
kõndiv = Kõndiv()
ujuv = Ujuv()

koer = KoerComp(loom, kõndiv)
koer.kõnni()
inimene = InimeneComp3(loom, kõndiv)
inimene.söö()
kuldkala = KuldkalaComp(loom, ujuv)
kuldkala.uju()
part = PartComp(loom, kõndiv, ujuv)
part.uju()
part.kõnni()

print("-"*30)

# Ilma IoC kasutuseta
class InimeneComp4():
    def __init__(self):
        self.__loom = Loom()
        self.__kõndiv = Kõndiv()
    def söö(self):
        self.__loom.söö()
    def maga(self):
        self.__loom.maga()
    def kõnni(self):
        self.__kõndiv.kõnni()

# Kasutamine

inimene = InimeneComp4()
inimene.kõnni()

print("-"*30)

# Kasutame seadistuste klassi ja tehas-klassi

class Seadistused:
    loom: Loom = None
    kõndiv: Kõndiv = None
    ujuv: Ujuv = None

class AnimalFactory:
    @staticmethod
    def LooKoer():
        return KoerComp(Seadistused.loom, Seadistused.kõndiv)

    @staticmethod
    def LooInimene():
        return InimeneComp3(Seadistused.loom, Seadistused.kõndiv)

    @staticmethod
    def LooKuldkala():
        return KuldkalaComp(Seadistused.loom, Seadistused.ujuv)

    @staticmethod
    def LooPart():
        return PartComp(Seadistused.loom, Seadistused.kõndiv, Seadistused.ujuv)


# Rakendust initsialiseerides saame seaidtuse omistada, välisest failist sisse lugeda vms
Seadistused.loom = Loom()
Seadistused.kõndiv = Kõndiv()
Seadistused.ujuv = Ujuv()

# Edasi saame oma klasse luua läbi tehas-klasside
inimene5 = AnimalFactory.LooInimene()
inimene5.maga()
koer5 = AnimalFactory.LooKoer()
koer.kõnni()
kala5 = AnimalFactory.LooKuldkala()
kala5.uju()
part5 = AnimalFactory.LooPart()
part5.kõnni()
part5.uju()
