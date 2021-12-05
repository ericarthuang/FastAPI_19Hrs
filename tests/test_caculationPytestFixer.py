import pytest
from app.caculation import add, substract, multiply, divide, BankAccount, InsuficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount(0)


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])                        
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
    

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50
    
def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30
    
def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70
    
def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 50.5
    

@pytest.mark.parametrize("deposited, withdraw, expected",
                         [
                             (200, 100, 100),
                             (50, 10, 40),
                             (1200, 200, 1000),
                         ])

def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected
    
def test_insuficient_funds(bank_account):
    with pytest.raises(InsuficientFunds):
        bank_account.withdraw(200)
    
    
