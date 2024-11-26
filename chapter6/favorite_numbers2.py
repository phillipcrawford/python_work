favorite_numbers = {
    'phil': [16777216], 
    'bob': [27, 36], 
    'paul':[47], 
    'koopman': [200], 
    'albert': [49]
    }
print(f"Phil's favorite number is {favorite_numbers['phil']}")
print(f"Bob's favorite number is {favorite_numbers['bob']}")
for name, numbers in favorite_numbers.items():
    print(f"\n{name}")
    for number in numbers:
        print(number)