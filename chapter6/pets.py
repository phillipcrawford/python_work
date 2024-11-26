birdie = {'species': 'bird', 'owner': 'paul'}
kitty = {'species': 'cat', 'owner': 'phil'}
doggy = {'species': 'dog', 'owner': 'ralph'}
pets = [birdie, kitty, doggy]
for pet in pets:
    print(f"the {pet['species']} is owned by {pet['owner']}")