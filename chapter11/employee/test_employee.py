import pytest
from employee import Employee

@pytest.fixture
def billy_employee():
    """An employee that will be available to all test functions"""
    billy_employee = Employee('billy', 'joe', 50000)
    return billy_employee

def test_give_default_raise(billy_employee):
    billy_employee.give_raise()
    assert billy_employee.salary == 55000

def test_give_custom_raise(billy_employee):
    billy_employee.give_raise(6000)
    assert billy_employee.salary == 56000