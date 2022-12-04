from Personaje import Personaje

class Enano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida="", daño="", bonificacion="", clan=""):
        super().__init__
        self.__clan = clan
    
    def str(self):
        super().str
        return " Bonificación : {}"
    
    def GetClan(self):
        return self.__clan
    def SetClan(self,clan):
        self.__clan = clan
    