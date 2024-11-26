cities = {
    'los angelos': {
        'country': 'USA',
        'population': 6_500_000,
        'fact': 'gets lots of water from norcal',
        }, 
    'santa barbara': {
        'country': 'USA',
        'population': 120_000,
        'fact': 'birthplace of phillip crawford!',
        }, 
    'san francisco': {
        'country': 'USA',
        'population': 900_000,
        'fact': 'likely to see a human defecate in public ~once a week!'
    }}
for city, facts in cities.items():
    print(f"\n{city}")
    for key, value in facts.items():
        print(f"{key} : {value}")