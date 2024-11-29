def city_country(city, country):
    location = f"{city.title()} is in {country.title()}"
    return(location)

san = city_country("santiago", "chile")
print(san)
los = city_country("los angelos", "usa")
print(los)
mex = city_country("mexico city", "mexico")
print(mex)