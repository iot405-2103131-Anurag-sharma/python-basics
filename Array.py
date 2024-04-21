#1
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# 
array1 = [1, 2, 3, 4, 5]
print("Sum of array elements:", sum_of_array(array1))
  

#2
def average_of_array(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

# 
array2 = [10, 20, 30, 40, 50]
print("Average of array elements:", average_of_array(array2))

#3
def find_index(arr, element):
    if element in arr:
        return arr.index(element)
    else:
        return -1

# 
array3 = [5, 10, 15, 20, 25]
element_to_find = 15
print("Index of element", element_to_find, "is:", find_index(array3, element_to_find))

#4
def contains_value(arr, value):
    return value in arr

# 
array4 = [1, 2, 3, 4, 5]
value_to_check = 3
print("Array contains", value_to_check, ":", contains_value(array4, value_to_check))

#5
def remove_element(arr, element):
    if element in arr:
        arr.remove(element)
    return arr

# 
array5 = [10, 20, 30, 40, 50]
element_to_remove = 30
print("Array after removing", element_to_remove, ":", remove_element(array5, element_to_remove))
#6
def copy_array(arr):
    return arr.copy()

# 
array6 = [1, 2, 3, 4, 5]
new_array6 = copy_array(array6)
print("Copied array:", new_array6)

#7
def insert_element(arr, element, position):
    arr.insert(position, element)
    return arr

# 
array7 = [1, 2, 4, 5]
element_to_insert = 3
position_to_insert = 2
print("Array after inserting", element_to_insert, "at position", position_to_insert, ":",
      insert_element(array7, element_to_insert, position_to_insert))

#8
def min_max_values(arr):
    if len(arr) == 0:
         return None, None
    return min(arr), max(arr)

# 
array8 = [10, 5, 20, 8, 15]
min_value, max_value = min_max_values(array8)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

#9
def reverse_array(arr):
    return arr[::-1]

# 
array9 = [1, 2, 3, 4, 5]
print("Reversed array:", reverse_array(array9))

#10
def find_duplicates(arr):
    duplicates = []
    for i in arr:
        if arr.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

# 
array10 = [1, 2, 3, 4, 5, 2, 3, 6]
print("Duplicate values:", find_duplicates(array10))


#11

def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

# 
array11_1 = [1, 2, 3, 4, 5]
array11_2 = [4, 5, 6, 7, 8]
print("Common elements:", find_common_elements(array11_1, array11_2))

#12
def remove_duplicates(arr):
    return list(set(arr))

# 
array12 = [1, 2, 3, 4, 5, 2, 3, 6]
print("Array after removing duplicates:", remove_duplicates(array12))

#13
def second_largest(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    if len(unique_elements) < 2:
        return 
    return unique_elements[-2]

# 
array13 = [10, 20, 5, 30, 40]
print("Second largest number:", second_largest(array13))

#14
def second_smallest(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    if len(unique_elements) < 2:
        return 
    return unique_elements[1]

# 
array14 = [10, 20, 5, 30, 40]
print("Second smallest number:", second_smallest(array14))

#15
def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

# 
array15 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count_even_odd(array15)
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

#16
def difference_of_max_min(arr):
    if len(arr) == 0:
        return 
    return max(arr) - min(arr)

# 
array16 = [10, 20, 5, 30, 40]
print("Difference of max and min:", difference_of_max_min(array16))

#17
def contains_two_elements(arr):
    return all(elem in arr for elem in (12, 23))



