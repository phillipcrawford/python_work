import t_user

class Priviledges:

    def __init__(self, priviledges):
        self.priviledges = priviledges

    def show_priviledges(self):
        for priviledge in self.priviledges:
            print(f"Admin: {priviledge}")

class Admin(t_user.User):

    def __init__(self, first_name, last_name, age, quote, priviledges):
        super().__init__(first_name, last_name, age, quote)
        self.priviledges = Priviledges(priviledges)