import random

class Parchis:
   #Variableses taticas
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0
   #Variableses no taticas
    def __init__(self, nomJ1, nomJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nomJ1 = nomJ1
        self.nomJ2 = nomJ2

   #Coge por parametro self devuelve la suma de dos numeros entre 1 y 6
    def tirarDados(self):
        Parchis.dado1 = random.randint(1, 6)
        Parchis.dado2 = random.randint(1, 6)
        return Parchis.dado1 + Parchis.dado2
    
   #Coge por parametro self devuelve una cadena mostrando la situacion de la partida
    def pintaTablero(self):
        res = "\t" + "\t".join([str(x) for x in range(Parchis.TAM_TABLERO)]) + "\n"
        res += self.nomJ1 + "  \t"
        for x in range(Parchis.TAM_TABLERO):
            if x == self.fichaJ1:
                res += "J1\t"
            else:
                res += "-\t"
        res += "\n" + self.nomJ2 + "  \t"
        for x in range(Parchis.TAM_TABLERO):
            if x == self.fichaJ2:
                res += "J2\t"
            else:
                res += "-\t"
        return res

    #Coge por parametro self y el nombre del jugador dependiendo del nombre modifica las variables 1 o 2 la funcion llama a tirarDados() suma el resultado a las variable ficha y si es mayopr le resta la diferencia no retorna nada 
    def avanzaPosiciones(self, nombreJugador):
        avance= self.tirarDados()
        if nombreJugador == self.nomJ1:
            self.fichaJ1 +=avance
            if self.fichaJ1 > Parchis.TAM_TABLERO:
                casillasPasadas = self.fichaJ1 - Parchis.TAM_TABLERO
                self.fichaJ1 = Parchis.TAM_TABLERO - casillasPasadas
        if nombreJugador == self.nomJ2:
            self.fichaJ2 += avance
            if self.fichaJ2 > self.TAM_TABLERO:
                casillasPasadas = self.fichaJ2 - Parchis.TAM_TABLERO
                self.fichaJ2 = Parchis.TAM_TABLERO - casillasPasadas

    #Coge por parametro self si y compara las fichas entre ellas y devuelve el resultado de la comparaciond de poscisiones en una cedena
    def estadoCarrera(self):
        res=""
        if self.fichaJ1 > self.fichaJ2:
            res= "Va ganando el jugador " + self.nomJ1
        elif self.fichaJ1 < self.fichaJ2:
            res= "Va ganando el jugador "+ self.nomJ2
        else:
            res= "Empate"
        return res

    #Coge por parametro self si self.fichaJ1 o fichaJ2 iguala res al nombre del jugador si no a Empate devuleve la cadena
    def esGanador(self):
        res=""
        if self.fichaJ1 == Parchis.TAM_TABLERO:
            res=  "El ganador es " + self.nomJ1
        elif self.fichaJ2 == Parchis.TAM_TABLERO:
            res= "El ganador es "+ self.nomJ2
        else:
            res= "Empate"
        return res

