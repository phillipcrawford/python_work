current_users = ["admin", "phil", "paul", "koopman", "crawford"]
new_users = ["admin", "koopman", "jon", "andrew", "alice"]
for new_user in new_users:
    if new_user in current_users:
        print(f"The username {new_user} has already been taken :(")
        print("Please select a new username")
    else:
        print(f"This username, {new_user} is available!")