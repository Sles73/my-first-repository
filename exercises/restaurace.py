class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine} cuisine.")

    def restaurant_open(self):
        print(f"{self.restaurant_name} is now open.")

my_restaurant = Restaurant("pepes_restaurant","italiano")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine)

my_restaurant.describe_restaurant()
my_restaurant.restaurant_open()

      



