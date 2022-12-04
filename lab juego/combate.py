from Personaje import Personaje
from Enano import Enano
from Humano import Humano
from Elfo import Elfo
from random import randint



elfo = Elfo()
humano = Humano
enano = Enano()

lista_elfos = []
lista_humanos = []
lista_enanos = []

selectlista1 = randint(1,3)
selectlista2 = randint(1,3)


selectp1 = randint(0,2)
selectp2 = randint(0,2)

while selectp1 == selectp2:
    selectp2 = randint(0,2)

if selectlista1 == 1:
    elfo = elfo[selectp1]

if selectlista1 == 2:
    humano = humano[selectp1]

if selectlista1 == 3:
    enano = enano[selectp1]

if selectlista2 == 1:
    elfo2 = elfo[selectp1]

if selectlista2 == 2:
    humano2 = humano[selectp1]

if selectlista2 == 3:
    enano2 = enano[selectp1]

b=1
while b<10 :
    if elfo.getNombre() != "":
      pass

    if humano.getNombre() != "":
        pass
    
    if enano.getNombre() != "":
        pass
    
    if elfo2.getNombre() != "":
        pass
    
    if humano2.getNombre() != "":
        pass
    
    if enano2.getNombre() != "":
        pass
    
    b+=1



    def combate(selectp1, selectp2):

        selectp1 = Personaje("","","","","","")
        selectp2 = Personaje("","","","","","")
        for i in range (10):
            print ("combate")

            if selectp1 or selectp2 == Elfo:
                return selectp1.GetVida - (selectp1.GetVida*0,1) or selectp2.GetVida - (selectp2.GetVida*0,1)
            elif selectp1 or selectp2 == Humano:
                try:
                  aumento_daño = input(int("escriba la cantidad de aumento de daño (entre 0 y 15)"))
                  if aumento_daño < 0 or aumento_daño > 15:
                
                
                    print("caracter no valido")
                except ValueError:
            
                    print("no se permite esa cantidad")
                    return selectp1.SetDaño = (selectp1.GetDaño + aumento_daño) or selectp2.SetDaño = (selectp1.GetDaño + aumento_daño)
            elif selectp1 or selectp2 == Enano:
                try:
                    aumenta_vida = input(int("ingrese la cantidad de aumento de vida (entre 50 y 100)"))  
                    if aumenta_vida < 50 or aumenta_vida > 100:
                        print ("no se permite esa cantidad")   
                    return selectp1.SetVida = (selectp1.GetVida + aumenta_vida) or selectp2.SetVida = (selectp1.GetVida + aumenta_vida)


                except ValueError:
                    print("caracter no valido")
                return selectp1.GetDaño - (selectp1.GetVida*0,1) or selectp2.GetVida - (selectp2.GetVida*0,1)
            if selectp1.GetVida < 0: or selectp2.GetVida < 0:
                break
            selectp1.SetVida = selectp1.GetVida - selectp2.GetDaño
            selectp1.SetVida = selectp2.GetVida - selectp1.GetDaño
            print("la vida del personaje es ", selectp1.SetVida)
            print("la vida del personaje es ", selectp2.SetVida)


            
            if selectp1 == Elfo and selectp1.GetVida < 0 or selectp1 == Elfo and selectp2.GetVida < 0:
                return Personaje.Historia
            elif selectp1 == Humano and selectp1.GetVida < 0 or selectp2 == Humano and selectp1.GetVida < 0:
                return ("Humano ha sido derrotado, actualizar arma")
            elif selectp1 == Enano and selectp1.GetVida < 0 or selectp2 == Enano and selectp1.GetVida < 0:
                return ("Enano ha sido derrotado")







            
