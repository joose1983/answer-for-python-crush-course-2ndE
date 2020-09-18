class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} must be famous in China")

    def open_restaurant(self):
        print(f"{self.restaurant_name} now is open")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.cuisine_type='western'
        self.flavors=['chockolate','strawberry','pear']

    def display_flavors(self):
        print("here are the icecream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

        
my_icecream=IceCreamStand('little shop','western')
my_icecream.display_flavors()

    
