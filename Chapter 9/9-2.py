class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} must be famous in China")

    def open_restaurant(self):
        print(f"{self.restaurant_name} now is open")

restaurant1=Restaurant('7 days hotel','Chinese')
restaurant2=Restaurant('homeinn', 'Chinese')
restaurant3=Restaurant('Hilton', 'French')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
