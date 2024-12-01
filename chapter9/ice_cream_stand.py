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

class IceCreamStand(Restaurant):
    """Represent an Ice Cream Stand child of Restaurant Class"""

    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()} is a flavor at {self.name.title()}")
    
ice = IceCreamStand('alimentos', 'italian', ['pistachio', 'mango', 'vanilla', 'chocolate'])
ice.show_flavors()
        