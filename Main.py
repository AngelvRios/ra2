from Clase_carta import carta
from Clase_albun import Albun
# from Tenglo_anime import partida

if __name__ == "__main__":
    on = True

    while (on == True):
        print ("TENGLO_ANIME\n[1] Jugar\n[2] Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            from Tenglo_anime import partida
            
            juego = partida
            juego()
            
        if opcion == "2":
            on = False

        else:
            print ("Opcion no existente")       

 


    
    