pizzas = ["pepperoni", "cheese", "neapolitan"]
for pizza in pizzas:
    print(f"Here's a type of pizza: {pizza.title()}")
print("\nUnpopular opinion, I don't care for pizza. The ratios are all wrong. Lots of bread, lots of cheese, not much else")
friend_pizzas = pizzas[:]
pizzas.append("pesto")
friend_pizzas.append("clam and garlic")
print(f"My favorite pizzas are {pizzas}")
print(f'My friend\'s favorite pizzas are {friend_pizzas}')