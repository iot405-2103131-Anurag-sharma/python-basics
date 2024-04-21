#1
# Generating Arithmetic Exception
result = 10 / 0
print(result)  # This line will not be reached

#2
# Handle Arithmetic Exception using try-catch block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught an Arithmetic Exception: Division by zero!")

#3
# Method that throws exception
def divide_by_zero():
    result = 10 / 0

# Call the method without try block (exception will propagate)
divide_by_zero()


#4
try:
    # Some code that might raise different exceptions
    result = 10 / 0
    file = open("non_existing_file.txt", "r")
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
except FileNotFoundError:
    print("Caught FileNotFoundError!")
except Exception as e:
    print("Caught an unexpected Exception:", e)

#5
try:
    raise Exception("Custom Exception Message")
except Exception as e:
    print("Caught Exception with Custom Message:", e)

#6
# Define a custom exception class
class CustomException(Exception):
    pass

# Raise the custom exception
try:
    raise CustomException("Custom Exception Raised!")
except CustomException as e:
    print("Caught Custom Exception:", e)


#7
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
finally:
    print("This will always execute whether an exception is caught or not.")

#8
# Generating Arithmetic Exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught Arithmetic Exception: Division by zero!")

#9
# Generating Arithmetic Exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught Arithmetic Exception: Division by zero!")
