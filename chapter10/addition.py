first_number = input('Please enter your first number: ')
second_number = input('Please enter your second number: ')
try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print("invalid input, only numbers will work")
else:
    print(sum)