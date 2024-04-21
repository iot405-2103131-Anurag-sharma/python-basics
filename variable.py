def my_function():
  # This is a local variable
  local_variable = 10

  # Print the value of the local variable
  print(local_variable)

# Call the function
my_function()

# Try to access the local variable outside of the function
# This will cause an error
print('local_variable')




# This is a global variable
global_variable = "I am a global variable"

def display_global():
    # Accessing the global variable inside this function
    print(global_variable)

def modify_global():
    global global_variable  # Declare that we're using the global variable
    global_variable = "I've been modified"

display_global() 
modify_global()
display_global()