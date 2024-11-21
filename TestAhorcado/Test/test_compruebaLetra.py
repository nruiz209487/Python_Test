from TestAhorcado.Ahorcado import *


def test_compruebaLetraNoCorrecta():
    res = False
    letra="a"
    obj =  Ahorcado()
    obj.compruebaLetra("a")
    res = letra in obj.noAcertadas
    res = obj
    assert res