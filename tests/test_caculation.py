from app.caculation import add, substract, multiply, divide

def test_add():
    print("testing add function")
    assert add(5, 3) == 8
    
    
def test_substract():
    print("testing add function")
    assert substract(5, 3) == 2
    
    
def test_multiply():
    print("testing add function")
    assert multiply(5, 3) == 15
    
    
def test_divide():
    print("testing add function")
    assert divide(6, 3) == 2
