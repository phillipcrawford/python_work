favorite_places = {
    'andrew': ['the park', 'the woods', 'the beach'],
    'bob': ['the mountains', 'the museum'],
    'curt': ['inside']
    }
for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are: ")
    for place in places:
        print(f"{place}")