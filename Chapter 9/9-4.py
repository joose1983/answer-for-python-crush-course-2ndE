class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} must be famous in China")

    def open_restaurant(self):
        print(f"{self.restaurant_name} now is open")

    def show_number_served(self):
        print(f"the restaurant {self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, number):
        if number >0:
            self.number_served = number
        else:
            print("the number_served cannot equal or below 0")

    def increment_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("the increment cannot less than number_served")

            
restaurant=Restaurant('7 days hotel','Chinese')
restaurant.show_number_served()
restaurant.increment_number_served(20)
restaurant.show_number_served()
restaurant.increment_number_served(50)
restaurant.show_number_served()
