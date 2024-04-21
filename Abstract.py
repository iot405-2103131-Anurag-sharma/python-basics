from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("This is a non-abstract method in the abstract class")

# Uncomment this line to see the error when trying to instantiate an abstract class
# abstract_obj = AbstractClass()




class SubClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method in SubClass")

# Creating an instance of SubClass
sub_obj = SubClass()
sub_obj.abstract_method()  # Implementation of the abstract method in SubClass
sub_obj.non_abstract_method()  # This is a non-abstract method in the abstract class




class SubClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method in SubClass")

    def call_methods(self):
        # Calling abstract method
        self.abstract_method()

        # Calling non-abstract method
        self.non_abstract_method()

        # Trying to call an undefined method
        # This will raise an AttributeError
        # Uncomment this line to see the error
        # self.undefined_method()

    def undefined_method(self):
        print("This method is not defined in the parent class")

    def create_instance_and_call_methods(self):
        # Creating an instance of SubClass inside SubClass
        sub_obj = SubClass()
        print("\nInside SubClass:")
        sub_obj.abstract_method()  # Implementation of the abstract method in SubClass
        sub_obj.non_abstract_method()  # This is a non-abstract method in the abstract class
        sub_obj.undefined_method()  # This method is not defined in the parent class

# Creating an instance of SubClass
sub_obj = SubClass()
print("Outside SubClass:")
sub_obj.call_methods()  # Implementation of the abstract method in SubClass
sub_obj.create_instance_and_call_methods()
