# 1. Creating a dictionary with Student IDs and Names
student_dict = {
    101: 'Anurag',
    102: 'Annu',
    103: 'Sharma',
    104: 'shikhar',
    105: 'upadhyay'
}

# 1.1. Adding values to the dictionary
student_dict[106] = 'Annu'
print("1.1. After Adding New Value:")
print(student_dict)

# 1.2. Updating values in the dictionary
student_dict[104] = 'Adarsh'
print("\n1.2. After Updating Value:")
print(student_dict)

# 1.3. Accessing a value in the dictionary
print("\n1.3. Accessing Value for Student ID 102:")
print(student_dict[102])

# 1.4. Creating a nested dictionary (Student ID, Name, and Age)
nested_dict = {
    101: {'Name': 'Annu', 'Age': 20},
    102: {'Name': 'Bobby', 'Age': 21},
    103: {'Name': 'Chotu', 'Age': 22}
}

# 1.5. Accessing values of the nested dictionary
print("\n1.5. Accessing Values of Nested Dictionary:")
for student_id, details in nested_dict.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {details['Name']}")
    print(f"Age: {details['Age']}")

# 1.6. Printing keys present in a particular dictionary
print("\n1.6. Keys Present in the Student Dictionary:")
for key in student_dict.keys():
    print(key)

# 1.7. Deleting a value from the dictionary
del student_dict[106]
print("\n1.7. After Deleting Value:")
print(student_dict)
