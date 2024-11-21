from TestAhorcado.Ahorcado import *

def test_compruebaPalabraNoCorrecta():
    res = False
    pablabraParametro = "pacio"
    obj =  Ahorcado()
    palabraPistaAntesDeActualizar =obj.palabraPista
    obj.compruebaPalabra("")
    if (pablabraParametro not in Ahorcado.Palabras):
        res = palabraPistaAntesDeActualizar==obj.palabraPista
    assert res