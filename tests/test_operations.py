from src.math_operations import add, sub

def test_add():
    assert add(3,2) == 5
    assert add(-1, 3) == 2
    
def test_sub():
    assert sub(3,2) == 1
    assert sub(5,7) == -2
    assert sub(-1,4) == -5
    assert sub(1,1) == 0