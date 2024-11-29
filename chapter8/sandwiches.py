def sandwich_maker(*toppings):
    for topping in toppings:
        print(f"Adding {topping} to your sandwich.")
    print("\n")

sandwich_maker('bacon', 'lettuce', 'tomato')
sandwich_maker('apple', 'brie', 'ham', 'blueberry')
sandwich_maker('ruffles', 'french fries')