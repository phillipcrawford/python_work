class User:
    """A simple representation of a User"""
    
    def __init__(self, first_name, last_name, age, quote):
        """initialize the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.quote = quote

    def describe_user(self):
        stri = f"{self.first_name.title()} {self.last_name.title()} is "
        stri += f"{self.age} years old and is known for saying "
        stri += f'"{self.quote}"'
        print(stri)
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

phil = User('Phillip', 'Crawford', 38, "yeet yeet yeet")
phil.describe_user()
phil.greet_user()
print(phil.age)        