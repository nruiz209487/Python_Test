from encriptacion_mensaje import encriptacion_mensaje

def test_encriptacion_mensaje():
    assert encriptacion_mensaje('hola',0)=='hola'

def test_encriptacion_mensaje2():
    assert encriptacion_mensaje('abcd',1)=='bcde'

def test_encriptacion_mensaje3():
    assert encriptacion_mensaje('abcd',2)=='cdef'

def test_encriptacion_mensaje4():
    assert encriptacion_mensaje('z',1)=='a'
    
def test_encriptacion_mensaje5():
    assert encriptacion_mensaje('b',-1)=='a'