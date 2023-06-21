from Clase_carta import carta

class Albun:
    def __init__(self):
        self.capacidad = 10
        self.baraja = []

    def agregar_cartas(self):
        
        card = carta("soldado")

        if len(self.baraja) < self.capacidad:
            i = len(self.baraja)
            i = i + 1
            self.baraja.append(card)

        if len(self.baraja) == self.capacidad:
            print("baraja llena")