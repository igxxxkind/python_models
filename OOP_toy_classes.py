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


