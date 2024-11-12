from Suma.suma import suma

def test_suma():
    assert suma(2,3)==5

def test_suma2():
    assert suma(-1,3)==2

def test_suma3():
    assert suma(1,-3)==-2