from JuegoDelParchis.Parchis import *

def test_pintaTablero():
    objetoParchis =  Parchis("Jug1","Jug2")
    assert objetoParchis.pintaTablero()==5

