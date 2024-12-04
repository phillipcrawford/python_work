from employee import Employee

def test_give_default_raise():
    billy = Employee('billy', 'joe', 50000)
    billy.give_raise()
    assert billy.salary == 55000

def test_give_custom_raise():
    bobby = Employee('bobby', 'bogen', 54000)
    bobby.give_raise(6000)
    assert bobby.salary == 60000