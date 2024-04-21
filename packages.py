class Class1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Class1, {self.name}!")

class Class2:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome from Class2, {self.name}!")





# Create objects for Class1 and Class2
class1_obj = Class1("Alice")
class2_obj = Class2("Bob")

# Call methods of Class1 and Class2
class1_obj.greet()
class2_obj.welcome()
