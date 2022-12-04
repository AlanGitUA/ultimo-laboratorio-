from Personaje import Personaje

class Elfo(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificacion="", reino=""):
        super().__init__
        self.__reino = reino
    
    def GetReino(self):
        return self.__reino
    
    def SetReino(self,reino):
        self.__reino = reino
