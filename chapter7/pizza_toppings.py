prompt = "\nAdd a topping to your pizza!"
prompt += "\nEnter 'quit' when you're done: "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"\nAdding {topping} to your pizza")