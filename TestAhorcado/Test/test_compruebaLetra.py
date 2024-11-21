from TestAhorcado.Ahorcado import *


def test_compruebaLetra():
    res = True
    obj =  Ahorcado()
    obj.compruebaLetra("")
    
    assert res