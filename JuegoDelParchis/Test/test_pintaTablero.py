from JuegoDelParchis.Parchis import *

def test_pintaTableroPosicion0():
    objetoParchis = Parchis("Jug1", "Jug2")
    objetoParchis.fichaJ1 = 0  
    objetoParchis.fichaJ2 = 3  
    resultado = objetoParchis.pintaTablero()
    expected_output = (
        "\t" + "\t".join([str(x) for x in range(20)]) + "\n" +
        "Jug1  \tJ1\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t\n" +
        "Jug2  \t-\t-\t-\tJ2\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t"
    )
    assert resultado == expected_output

