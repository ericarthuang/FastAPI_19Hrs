import pytest
from app.caculation import add, substract, multiply, divide, BankAccount


@pytest.mark.parametrize("num1, num2, expected", 
                         [(3, 2, 5),
                          (7, 1, 8),
                          (12, 4, 16)])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected
    
    
def test_substract():
    print("testing add function")
    assert substract(5, 3) == 2
    
    
def test_multiply():
    print("testing add function")
    assert multiply(5, 3) == 15
    
    
def test_divide():
    print("testing add function")
    assert divide(6, 3) == 2
    

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50
    
def test_bank_default_amount():
    bank_account = BankAccount()
    assert bank_account.balance == 0
    
def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30
    
def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70
    
def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 50.5
    
    
    

