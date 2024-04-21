#1
# Using single quotes
string1 = 'Hello, World!'

# Using double quotes
string2 = "Hello, World!"

# Using triple quotes for multi-line strings
string3 = '''This is a
multi-line
string'''

print(string1)
print(string2)
print(string3)

#2
string1 = "Hello"
string2 = "World"

result = string1 + " " + string2
print(result)

#3
string = "Hello, World!"
length = len(string)
print("Length of the string:", length)

#4
string = "Hello, World!"

# Extracting substring from index 7 to end
substring = string[7:]
print("Substring:", substring)

#5
string = "Hello, World!"

# Finding the index of "World"
index = string.index("World")
print("Index of 'World':", index)

#6
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "fox"

match = re.match(pattern, string)

if match:
    print("Pattern matched!")
else:
    print("Pattern not found!")

#7
string1 = "Hello"
string2 = "World"

if string1 == string2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#8
string = "Hello, World!"

# Check if string starts with "Hello"
if string.startswith("Hello"):
    print("String starts with 'Hello'")

# Check if string ends with "World!"
if string.endswith("World!"):
    print("String ends with 'World!'")

# Compare two strings
string1 = "apple"
string2 = "banana"

result = string1.casefold().compareto(string2.casefold())  # compareto() is not a built-in Python method, using str.casefold() for case-insensitive comparison
if result < 0:
    print("string1 comes before string2")
elif result > 0:
    print("string2 comes before string1")
else:
    print("Both strings are equal")

#9
string = "  Hello, World!  "

# Removing leading and trailing whitespace
trimmed_string = string.strip()

print("Original string:", string)
print("Trimmed string:", trimmed_string)

#10
string = "Hello, World!"

# Replace "Hello" with "Hi"
new_string = string.replace("Hello", "Hi")

print("Original string:", string)
print("New string:", new_string)

#11
string = "Hello, World!"

# Splitting the string by comma and space
split_string = string.split(", ")

print("Original string:", string)
print("Split string:", split_string)

#12
integer_num = 123

# Converting integer to string
string_num = str(integer_num)

print("Integer as string:", string_num)

#13
string = "Hello, World!"

# Converting to uppercase
uppercase_string = string.upper()

# Converting to lowercase
lowercase_string = string.lower()

print("Uppercase:", uppercase_string)
print("Lowercase:", lowercase_string)
