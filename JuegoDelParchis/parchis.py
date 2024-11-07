import random

class Parchis:
    TAM_TABLERO =20 
    def __init__(self,nomJ1,nomJ2):

        self.fichaJ1 =0
        self.fichaJ2 =0
        self.dado1 = 0
        self.dado2 = 0
        self.nomJ1 =nomJ1
        self.nomJ2 =nomJ2

    @staticmethod
    def tirarDados(self):
        self.dado1 = random.randint(1, 6)
        self.dado2 = random.randint(1, 6)
        return  self.dado1+ self.dado2
    
    @staticmethod
    def pintaTablero(self):
        res="/t"
        for i in range(0,self.TAM_TABLERO+1):
            res+=i + " "
        res+="F"
        return res


    @staticmethod
    def avanzaPosiciones(self,nombreJugador):
        if(nombreJugador== self.nomJ1):
            Parchis.fichaJ1= Parchis.tirarDados(self)
            if(Parchis.fichaJ1> self.TAM_TABLERO):
                casillasPasadas=Parchis.fichaJ1-self.TAM_TABLERO
                Parchis.fichaJ1=self.TAM_TABLERO
                Parchis.fichaJ1= Parchis.fichaJ1-casillasPasadas
        if(nombreJugador== self.nomJ2):
            Parchis.fichaJ2= Parchis.tirarDados(self)
            if(Parchis.fichaJ2> self.TAM_TABLERO):
                casillasPasadas=Parchis.fichaJ2-self.TAM_TABLERO
                Parchis.fichaJ2=self.TAM_TABLERO
                Parchis.fichaJ2= Parchis.fichaJ2-casillasPasadas

    @staticmethod
    def estadoCarrera(self):
        res=""
        if(Parchis.fichaJ1 > Parchis.fichaJ2):
            res="Va ganando el jugador 1 "
        elif(Parchis.fichaJ1 < Parchis.fichaJ2):
            res="Va ganando el jugador 2 "
        else:
            res="Empate"


    @staticmethod
    def esGanador(self):
        res=""
        return res
       


