from JuegoDelParchis.Parchis import *

def test_tirarDados():
    objetoParchis =  Parchis("Jug1","Jug2")
    assert objetoParchis.tirarDados()== 1 or 2 or 3 or 4 or 5 or 6

