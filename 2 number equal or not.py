def check_equality(num1, num2):
    if num1 == num2:
        return "The two numbers are equal."
    else:
        return "The two numbers are not equal."

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to check equality
result = check_equality(num1, num2)

# Display the result
print(result)
