from JuegoDelParchis.Parchis import *

def test_estadoCarrera():
    objetoParchis =  Parchis("Jug1","Jug2")
    assert objetoParchis.estadoCarrera()==5
