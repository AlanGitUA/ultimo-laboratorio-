from Personaje import Personaje

class Humano(Personaje):
    def __init__(self, tipo="", nombre="", raza="", arma="", vida="", daño="", bonificacion="", familia=""):
        super().__init__
        self.__familia = familia
    
    def GetFamilia(self):
        return self.__familia
    
    def SetFamilia(self,familia):
        self.__famiia = familia