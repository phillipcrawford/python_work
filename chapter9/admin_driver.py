from super_user import User, Admin, Priviledges

phil = User('Phillip', 'Crawford', 38, "yeet yeet yeet")
phil.describe_user()
phil.greet_user()
print(phil.age)
phil.increment_login_attempts()
phil.increment_login_attempts()
print(phil.login_attepmts)
phil.reset_login_attempts()
print(phil.login_attepmts)

admin = Admin('phil', 'crawford', 38, 'I am the admin', ['can add post', 'can delete post', 'can ban user'])
admin.priviledges.show_priviledges()