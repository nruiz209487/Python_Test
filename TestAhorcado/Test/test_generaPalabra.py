from TestAhorcado.Ahorcado import *

def test_generaPalabra():
    obj = Ahorcado()
    obj.generaPalabra()
    res = obj.palabraSecreta in Ahorcado.Palabras
    assert res