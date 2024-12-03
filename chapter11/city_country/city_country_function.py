def city_country(city, country, population=''):
    """Generate a neatly formatted location name"""
    if population:
        if country == 'USA':
            location = f"{city.title()}, {country} - population {population}"
        else:
            location = f"{city.title()}, {country.title()} - population {population}"
    else:
        if country == 'USA':
            location = f"{city.title()}, {country}"
        else: 
            location = f"{city.title()}, {country.title()}"
    return location