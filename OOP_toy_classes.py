class Dog():
    """A simple dog model
    """
    
    def __init__(self, name, age):
        """Simple attributes of a dog.
       
        """
        self.name = name
        self.age = age
        
    def sit(self):
        """A dog sits by  a command
        """
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        """
        """
        print(f"{self.name} rolled over!")
        
        
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

class User():
    
    def __init__(self, fname, lname, age, sex, access):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex
        self.access = access

    def describe_user(self):
        print(f"{self.fname} {self.lname} is {self.age} year(s) old, {self.sex}, and has {self.access} access type.")
    
    def greet_user(self):
        print(f"Good morning, {self.fname.title()} {self.lname.title()}")
        
blue = User('Ivan', 'Cocky', 24, 'male', 'basic')
blue.greet_user()
white = User('Boris', 'The Blade', 48, 'female', 'basic' )

class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        

my_new_car = Car('audi', 'A4', 2019)
my_new_car.get_descriptive_name()

my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(12)
my_new_car.update_odometer(32)
my_new_car.read_odometer()

my_other_car = Car('subaru', 'outback', 2015)

my_other_car.get_descriptive_name()

my_other_car.update_odometer(23_500)
my_other_car.read_odometer()

my_other_car.increment_odometer(100)
my_other_car.read_odometer()

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWh size battery.")
        
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


