def plusone(x):
    return x+1
def test_one():
    assert plusone(3) == 5
def test_2():
    #comparison
    assert 'foo 1 bar' == 'foo 2 bar'

def test_3():
    #comparison2
    a = 'a'*100+'1'+'b'*100
    b = 'a'*100+'2'+'b'*100
    assert a == b

def test_4():
    #comparison2
    a = set([1,2,3])
    b = set([1,3,4])
    assert a == b
    
def test_5():
    #comparison2
    a = set([1,2,3])
    b = set([1,3,4])
    assert a == b
def test_6():
    a={'a':'b'}
    b={'x':'d'}
    assert a == b