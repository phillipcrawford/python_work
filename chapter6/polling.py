favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
potential_polltakers = ['albert', 'phil', 'jason']
for people in potential_polltakers:
    if people in favorite_languages:
        print(f"{people} thank you for responding")
    else:
        print(f"{people} you should take the poll")