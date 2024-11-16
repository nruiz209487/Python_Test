from JuegoDelParchis.Parchis import *

def test_estadoCarreraEmpate():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 5
    objetoParchis.fichaJ2 = 5
    resultado = objetoParchis.estadoCarrera()
    assert resultado == "Empate"

def test_EstadoCarreraGanandoJug1():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 8
    objetoParchis.fichaJ2 = 5
    resultado = objetoParchis.estadoCarrera()
    assert resultado == "Va ganando el jugador Jug1"

def test_EstadoCarreraGanandoJug2():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 4
    objetoParchis.fichaJ2 = 7
    resultado = objetoParchis.estadoCarrera()
    assert resultado == "Va ganando el jugador Jug2"
