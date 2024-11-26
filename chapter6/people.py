phil = {'first_name': 'phil', 'last_name': 'crawford', 'age': 38, 'city': 'Bozeman'}
jon = {'first_name': 'jon', 'last_name': 'jacob', 'age': 35, 'city': 'Santa Barbara'}
barry = {'first_name': 'barry', 'last_name': 'oscar', 'age': 30, 'city': 'Boise'}
people = [phil, jon, barry]
for person in people:
    str1 = f"{person['first_name'].title()} {person['last_name'].title()}"
    str2 = f" is age {person['age']} and lives in {person['city']}"
    print(str1 + str2)