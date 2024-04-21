def compare_numbers(num1, num2):
    if num1 < num2:
        return num1, num2
    elif num1 > num2:
        return num2, num1
    else:
        return None, None

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to compare the numbers
smaller, larger = compare_numbers(num1, num2)

# Display the result
if smaller is not None and larger is not None:
    print(f"Smaller number: {smaller}")
    print(f"Larger number: {larger}")
else:
    print("Numbers are equal.")
