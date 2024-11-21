from TestAhorcado.Ahorcado import *

def test_compruebaPalabraNoCorrecta():
    res = False
    obj =  Ahorcado()
    palabraPistaAntesDeActualizar =obj.palabraPista
    obj.compruebaPalabra("")
    res = palabraPistaAntesDeActualizar==obj.palabraPista
    assert res


def test_compruebaPalabraCorrecta():
    res = False
    obj =  Ahorcado()
    obj.palabraSecreta="individuo"
    palabraPistaAntesDeActualizar =obj.palabraPista
    obj.compruebaPalabra("individuo")
    res = palabraPistaAntesDeActualizar!=obj.palabraPista and obj.palabraPista ==obj.palabraSecreta
    assert res


def test_compruebaPalabraCorrectaMayuscula():
    res = False
    obj =  Ahorcado()
    obj.palabraSecreta="mujer"
    palabraPistaAntesDeActualizar =obj.palabraPista
    obj.compruebaPalabra("MuJeR")
    res = palabraPistaAntesDeActualizar!=obj.palabraPista and obj.palabraPista ==obj.palabraSecreta
    assert res