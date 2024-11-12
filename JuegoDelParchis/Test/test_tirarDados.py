from JuegoDelParchis.Parchis import *

def test_tirarDados():
    objetoParchis =  Parchis("Jug1","Jug2")
    assert objetoParchis.tirarDados()==5

