usernames = []#["admin", "phil", "paul", "koopman", "crawford"]
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like a status report?")
        else:
            print(f"Hello {username}, welcome back!")
else:
    print("We need to find some users!")