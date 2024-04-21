#1
class MyClass:
    static_variable = "Static variable value"


print(MyClass.static_variable)

#2
class MyClass:
    static_variable = "Static variable value"


instance1 = MyClass()


print(instance1.static_variable)


#3
class MyClass:
    static_variable = "Static variable value"


instance2 = MyClass()


instance2.static_variable = "Modified static value"


print(instance2.static_variable)

print(MyClass.static_variable)

#4
class MyClass:
    static_variable = "Static variable value"


MyClass.static_variable = "Modified static value"


print(MyClass.static_variable)


instance3 = MyClass()


print(instance3.static_variable)
