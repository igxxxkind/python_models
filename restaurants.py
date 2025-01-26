
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} dishes")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is opened")
        
    def set_number_served(self, totals):
        self.number_served = totals

    def increment_number_served(self, number):
        self.number_served += number
            
local_one = Restaurant('Mleczny', 'Polish')
local_one.set_number_served(500)
local_one.increment_number_served(50)
new_one = Restaurant('Mir plova', 'Asian')
new_one.set_number_served(1000)
new_one.increment_number_served(100)
oriental_one = Restaurant('Habibi', 'Arabic')
oriental_one.set_number_served(650)
oriental_one.increment_number_served(65)

local_one.number_served
new_one.number_served
oriental_one.number_served

class IceCreamStand(Restaurant):
    def __init__(self)
