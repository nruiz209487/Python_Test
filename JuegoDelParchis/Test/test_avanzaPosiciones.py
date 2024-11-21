from JuegoDelParchis.Parchis import *


def test_avanzaPosicionesJug11():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 5
    objetoParchis.fichaJ2 = 10
    avance = 4 
    objetoParchis.tirarDados = lambda: avance # SUstitulle el tirar dados (si le he tenido que preguntar a chatgpt como realizar esto)
    objetoParchis.avanzaPosiciones("Jug1")
    assert objetoParchis.fichaJ1 == 9

def test_avanzaPosicionesJug2():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 3
    objetoParchis.fichaJ2 = 5
    avance = 6 
    objetoParchis.tirarDados = lambda: avance  # SUstitulle el tirar dados (si le he tenido que preguntar a chatgpt como realizar esto)
    objetoParchis.avanzaPosiciones("Jug2")
    assert objetoParchis.fichaJ2 == 11

def test_avanzaPosicionesMayorQueTablero():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 18  
    avance = 5 
    objetoParchis.tirarDados = lambda: avance   # SUstitulle el tirar dados (si le he tenido que preguntar a chatgpt como realizar esto)
    objetoParchis.avanzaPosiciones("Jug1") 
    assert objetoParchis.fichaJ1 == 17
