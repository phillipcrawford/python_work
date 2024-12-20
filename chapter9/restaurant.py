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