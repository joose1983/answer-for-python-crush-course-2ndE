class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} must be famous in China")

    def open_restaurant(self):
        print(f"{self.restaurant_name} now is open")


