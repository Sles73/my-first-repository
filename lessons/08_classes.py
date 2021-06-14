class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attribues."""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a comand"""
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        """simulate a dog rolling over in response to a comand"""
        print(f"{self.name} is now rolling over!")

my_dog = Dog("Darek",12)
print(f"My dog name is {my_dog.name}")
print(f"My dog age is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()



