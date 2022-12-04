class Personaje():
    def __init__(self, nombre="", raza="", arma="", vida=100, daño=10, bonificacion=""):

        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma 
        self.__vida = vida
        self.__daño = daño
        self.__bonificacion = bonificacion

    def str(self):
        return "Nombre : {}  -  Raza : {}  -  Arma : {}  -  Vida : {}  -  Daño : {}  -  Bonificación : {}"

    def GetNombre(self):
        return self.__nombre
    def GetRaza(self):
        return self.__raza
    def GetArma(self):
        return self.__arma
    def GetVida(self):
        return self.__vida
    def GetDaño(self):
        return self.__daño
    def GetBonif(self):
        return self.__bonificacion


    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetRaza(self,raza):
        self.__raza = raza
    def SetArma(self,arma):
        self.__arma = arma
    def SetVida(self,vida):
        self.__vida = vida
    def SetDaño(self,daño):
        self.__dñao = daño
    def SetBonif(self,bonificacion):
        self.__bonificacion =bonificacion

    
    def Combate(self):
        pass

    def Historia(self):
        pass

    def Victoria(self):
        pass

    def Derrota(self):
        pass

    def MensajeInicial(self):
        pass