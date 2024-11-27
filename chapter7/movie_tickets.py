prompt = "what is your age? "
age = input(prompt)
age = int(age)
price = 0
if age < 3:
    price = 0
elif age < 12:
    price = 10
else:
    price = 15
print(f"Your ticket price is ${price}") 
