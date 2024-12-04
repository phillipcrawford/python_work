class Employee:
    """represent an employee"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, sal_increase=5000):
        """reassign salaray by amount of salary increase"""
        self.salary += sal_increase