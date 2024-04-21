file_path = "sample.txt" #enter your file path  here

# Reading text from file
try:
    with open(file_path, "r") as file:
        text = file.read()
        print("Contents of the file:")
        print(text)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")


#2
file_path = "output.txt"
content = "This is a line written to the file."

# Writing text to file
try:
    with open(file_path, "w") as file:
        file.write(content)
    print("Content written to the file successfully.")
except IOError:
    print("Error writing to the file.")


#3
file_path = "sample.txt"

# Reading file stream
try:
    with open(file_path, "rb") as file:
        stream = file.read()
        print("File stream read successfully.")
        # Do something with the stream if needed
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

#4
file_path = "sample.txt"

# Reading file stream with random access
try:
    with open(file_path, "rb") as file:
        # Move to the 10th byte from the beginning
        file.seek(10)
        stream = file.read()
        print("File stream read with random access:")
        print(stream)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

#5
file_path = "sample.txt"

# Read from a specific index using seek()
try:
    with open(file_path, "r") as file:
        file.seek(20)  # Seek to the 20th character from the beginning
        text = file.read()
        print("Content from the 20th character:")
        print(text)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
#6
import os

file_path = "sample.txt"

# Check read and write access permissions
if os.access(file_path, os.R_OK):
    print("File has read access.")
else:
    print("File does not have read access.")

if os.access(file_path, os.W_OK):
    print("File has write access.")
else:
    print("File does not have write access.")


