#1
for A in range(10):
    print("Bright IT Career")


#2
num = 1

while num <= 20:
    print(num)
    num += 1

#3
def compare_fixed_numbers():
    num1 = 5
    num2 = 9

    if num1 == num2:
        return f"{num1} is equal to {num2}"
    elif num1 != num2:
        return f"{num1} is not equal to {num2}"
    else:
        return "Invalid comparison"

# Call the function to compare fixed numbers
result = compare_fixed_numbers()

# Display the result
print(result)

#4 even or odd
x = 24

if x % 24 == 0:
	print(x,"Is Even Number")
else:
	print(x, "Is Odd Number")
	
y = 19

if y % 19 == 0:
	print(y,"Is Even Number")
else:
	print(y, "Is Odd Number")




#5
num1, num2, num3 = 10 , 30 , 20
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)

#6
num = 10

print("Even numbers between 10 and 20:")
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1


#7
def is_armstrong(number):
    # Count the number of digits
    num_digits = len(str(number))

    # Initialize sum to 0
    sum_of_digits = 0
    temp = number

    # Calculate sum of digits each raised to the power of num_digits
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** num_digits
        temp //= 10

    # Check if the number is Armstrong
    if number == sum_of_digits:
        return True
    else:
        return False

# Taking input from the user
num = int(input("Enter a number: "))

# Call the function to check if it's an Armstrong number
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")





#8
num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#9
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


#10
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function with different numbers
num1 = 10
num2 = 7
num3 = 0

result1 = check_even_odd(num1)
result2 = check_even_odd(num2)
result3 = check_even_odd(num3)

print(f"{num1} is {result1}")
print(f"{num2} is {result2}")
print(f"{num3} is {result3}")



#11
def print_gender(gender):
    if gender == 'M':
        print("Gender: Male")
    elif gender == 'F':
        print("Gender: Female")
    else:
        print("Invalid input")

# Test the function with different inputs
input1 = 'M'
input2 = 'F'
input3 = 'X'  # Invalid input

print_gender(input1)
print_gender(input2)
print_gender(input3)



