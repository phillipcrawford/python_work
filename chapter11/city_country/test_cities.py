from city_country_function import city_country

def test_city_country():
    """Do locations like New York, New York work? """
    formatted_location = city_country('New York', 'New York')
    assert formatted_location == "New York, New York"