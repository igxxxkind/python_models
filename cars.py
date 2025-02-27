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
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh size battery.")
        
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size ==100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



