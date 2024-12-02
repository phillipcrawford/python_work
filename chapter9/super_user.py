class User:
    """A simple representation of a User"""
    
    def __init__(self, first_name, last_name, age, quote):
        """initialize the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.quote = quote
        self.login_attepmts = 0

    def describe_user(self):
        stri = f"{self.first_name.title()} {self.last_name.title()} is "
        stri += f"{self.age} years old and is known for saying "
        stri += f'"{self.quote}"'
        print(stri)
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attepmts += 1

    def reset_login_attempts(self):
        self.login_attepmts = 0

class Priviledges:

    def __init__(self, priviledges):
        self.priviledges = priviledges

    def show_priviledges(self):
        for priviledge in self.priviledges:
            print(f"Admin: {priviledge}")

class Admin(User):

    def __init__(self, first_name, last_name, age, quote, priviledges):
        super().__init__(first_name, last_name, age, quote)
        self.priviledges = Priviledges(priviledges)