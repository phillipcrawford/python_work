class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, name, type):
        """Initialize attributes to describe a car."""
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"{self.name.title()} is a {self.type} restaurant")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open!")

new_restaurant = Restaurant('faralitos', 'mexican')
print(new_restaurant.name)
print(new_restaurant.type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
second_restaurant = Restaurant('606', 'Chinese')
print(second_restaurant.name)
print(second_restaurant.type)
second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()
third_restaurant = Restaurant('Parthenon', "Greek")
print(third_restaurant.name)
print(third_restaurant.type)
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()