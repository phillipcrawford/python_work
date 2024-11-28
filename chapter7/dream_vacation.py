destinations = {}
prompt = "If you could go anywhere in the world, where would you go? "

while True:
    print("Enter 'quit' to exit")
    username = input("What is your name? ")
    if username == 'quit':
        break
    answer = input(prompt)
    if answer == 'quit':
        break
    elif username in destinations.keys():
        destinations[username].append(answer)
    else:
        destinations[username] = [answer]
print(destinations)