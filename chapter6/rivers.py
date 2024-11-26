rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'usa'}
for river, country in rivers.items():
    print(f"The {river} has it's delta in {country}")
for river in rivers:
    print(f"The {river}")
for country in rivers.values():
    print(f"The {country.title()}")