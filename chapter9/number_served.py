class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, name, type):
        """Initialize attributes to describe a car."""
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} is a {self.type} restaurant")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open!")

    def set_number_served(self, count):
        self.number_served = count

    def increment_number_served(self, count):
        self.number_served += count    

new_restaurant = Restaurant('faralitos', 'mexican')
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