from JuegoDelParchis.Parchis import *

def test_avanzaPosiciones():
    objetoParchis =  Parchis("Jug1","Jug2")
    assert objetoParchis.avanzaPosiciones()==5