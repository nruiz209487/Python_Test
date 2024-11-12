from JuegoDelParchis.Parchis import *

def test_esGanador():
    objetoParchis =  Parchis("Jug1","Jug2")
    assert objetoParchis.esGanador()==5