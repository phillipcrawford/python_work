import restaurant
new_restaurant = restaurant.Restaurant('faralitos', 'mexican')
print(new_restaurant.name)
print(new_restaurant.type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
print(new_restaurant.number_served)
new_restaurant.number_served = 6
print(new_restaurant.number_served)
new_restaurant.set_number_served(9)
print(new_restaurant.number_served)
new_restaurant.increment_number_served(8)
print(new_restaurant.number_served)