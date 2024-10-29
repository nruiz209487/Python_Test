from codigoDeBarras import codigoDeBarras


def test_codigoDeBarras1():
    assert codigoDeBarras(65839522)==True

def test_codigoDeBarras2():
    assert codigoDeBarras(65839521)==False

def test_codigoDeBarras3():
    assert codigoDeBarras(8414533043847)==True

def test_codigoDeBarras4():
    assert codigoDeBarras(5029365779425)==True
    
def test_codigoDeBarras5():
    assert codigoDeBarras(5129365779425)==False


    
