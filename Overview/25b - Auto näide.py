from abc import ABCMeta, abstractmethod
class IRool (metaclass = ABCMeta):
    @abstractmethod
    def keera(self):
        print("Mina ei oska tegelikult autot juhtida")

class TavalineRool(IRool):
    def keera(self):
        print("tavaline")

class SportRool(IRool):
    def keera(self):
        print("Sportrool")

    
class TavalineAuto:
    rool : IRool

    def __init__(self):
        self.rool = TavalineRool()

    def keera(self):
        self.rool.keera()

class SportAuto:
    rool : IRool

    def __init__(self):
        self.rool = SportRool()

    def keera(self):
        self.rool.keera()

class CustomAuto:
    rool : IRool

    def __init__(self, rool: IRool):
        self.rool = rool

    def keera(self):
        self.rool.keera()
    
minuAuto = CustomAuto(SportRool())
minuAuto.keera()