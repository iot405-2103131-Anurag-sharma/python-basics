class Example:
    def display(self, x):
        print("Method with one parameter:", x)

    def display(self, x, y):
        print("Method with two parameters:", x, y)

# Create an instance of the class
example_obj = Example()

# Call the methods with different number of parameters
example_obj.display(10)        # This will call the second display method
example_obj.display(20, 30)    # This will also call the second display method





#2

class Example:
    def display(self, x):
        print("Method with one parameter of type int:", x)

    def display(self, x, y):
        print("Method with two parameters of type int and str:", x, y)

# Create an instance of the class
example_obj = Example()

# Call the methods with different number of parameters and data types
example_obj.display(10)           # This will call the first display method with one parameter
example_obj.display(20, "Hello")  # This will call the second display method with two parameters


#3
class Example:
    def display(self, x, y=None):
        if y is None:
            print("Method with one parameter:", x)
        else:
            print("Method with two parameters:", x, y)

# Create an instance of the class
example_obj = Example()

# Call the methods with different number of parameters
example_obj.display(10)           # This will call the first display method with one parameter
example_obj.display(20, "Hello")  # This will call the second display method with two parameters
