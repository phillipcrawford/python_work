from employee import Employee

def test_give_default_raise():
    billy = Employee('billy', 'joe', 50000)
    billy.give_raise()
    assert billy.salary == 55000