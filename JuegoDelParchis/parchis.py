import random

class Parchis:
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0

    def __init__(self, nomJ1, nomJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nomJ1 = nomJ1
        self.nomJ2 = nomJ2

    def tirarDados(self):
        Parchis.dado1 = random.randint(1, 6)
        Parchis.dado2 = random.randint(1, 6)
        return Parchis.dado1 + Parchis.dado2

    def pintaTablero(self):
        res = ""
        return res

    def avanzaPosiciones(self, nombreJugador):
        if nombreJugador == self.nomJ1:
            self.fichaJ1 += self.tirarDados()
            if self.fichaJ1 > Parchis.TAM_TABLERO:
                casillasPasadas = self.fichaJ1 - Parchis.TAM_TABLERO
                self.fichaJ1 = Parchis.TAM_TABLERO - casillasPasadas
        if nombreJugador == self.nomJ2:
            self.fichaJ2 += self.tirarDados()
            if self.fichaJ2 > self.TAM_TABLERO:
                casillasPasadas = self.fichaJ2 - Parchis.TAM_TABLERO
                self.fichaJ2 = Parchis.TAM_TABLERO - casillasPasadas

    def estadoCarrera(self):
        res=""
        if self.fichaJ1 > self.fichaJ2:
            res= "Va ganando el jugador 1"
        elif self.fichaJ1 < self.fichaJ2:
            res= "Va ganando el jugador 2"
        else:
            res= "Empate"
        return res

    def esGanador(self):
        res=""
        if self.fichaJ1 == Parchis.TAM_TABLERO:
            res= "El ganador es {self.nomJ1}"
        elif self.fichaJ2 == Parchis.TAM_TABLERO:
            res= "El ganador es {self.nomJ2}"
        else:
            res= "Aún no hay ganador"
        return res

