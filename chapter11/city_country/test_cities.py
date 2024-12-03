from city_country_function import city_country

def test_city_country():
    """Do locations like Amsterdam, Netherlands work?"""
    formatted_location = city_country('amsterdam', 'netherlands')
    assert formatted_location == "Amsterdam, Netherlands"

def test_city_country_in_USA():
    """Do locations like New York, USA work?"""
    formatted_location = city_country('New York', 'USA', 7_000_000)
    assert formatted_location == "New York, USA - population 7000000"

def test_city_country_population():
    """Do locations like Mexico City, Mexico - population 10_000_000 work?"""
    formatted_location = city_country('los angelos', 'USA')
    assert formatted_location == 'Los Angelos, USA'

def test_city_country_population_in_USA():
    """Do locations like Los Angelos, USA - population 6_000_000 work?"""
    formatted_location = city_country('los angelos', 'USA', 6_000_000)
    assert formatted_location == 'Los Angelos, USA - population 6000000'