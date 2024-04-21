def compare_numbers(num1, num2):
    if num1 < num2:
        return f"{num1} is less than {num2}"
    elif num1 <= num2:
        return f"{num1} is less than or equal to {num2}"
    elif num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 >= num2:
        return f"{num1} is greater than or equal to {num2}"
    else:
        return "Numbers are not comparable."

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to compare the numbers
result = compare_numbers(num1, num2)

# Display the result
print(result)
