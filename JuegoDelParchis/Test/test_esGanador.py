from JuegoDelParchis.Parchis import *

def test_esGanadorEmpate():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 10
    objetoParchis.fichaJ2 = 15
    resultado = objetoParchis.esGanador()
    assert resultado == "Empate"

def test_esGanadorJug1():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = Parchis.TAM_TABLERO
    objetoParchis.fichaJ2 = 15
    resultado = objetoParchis.esGanador()
    assert resultado == "El ganador es Jug1"

def test_esGanadorJug2():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 12
    objetoParchis.fichaJ2 = Parchis.TAM_TABLERO
    resultado = objetoParchis.esGanador()
    assert resultado == "El ganador es Jug2"
