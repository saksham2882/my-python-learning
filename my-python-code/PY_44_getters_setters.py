# Demonstrates @property for getters and setters


# Getter: Used to get the value of a private variable.
# Setter: Used to set or modify the value of a private variable.

# normal
class MyClass:                                       # Class
    def __init__(self , value):                      # constructor with parameters(arguments)
        self._value = value                          # Private variable (conventionally)
        
    def show(self):                                  # Default constructor
        print(f"Value is {self._value}")    

    @property                                        # Decorators
    def ten_value(self):                             # Getter method
        return 10 * self._value

obj = MyClass(10)                                    # object
print(obj._value)
# obj.ten_value = 67                                 # show an error, because it is not a proper way for setter.
print(obj.ten_value)                                 # Getter
obj.show()


print("-------------------")


# Setter:-
class MyClass1:                                      # Class
    def __init__(self , value):                      # constructor with parameters(arguments)
        self._value = value                          # Private variable (conventionally)
        
    @property                                        # This decorator works as a getter function. It acts like a property but is actually a method.
    def ten_value(self):                             # Getter method
        return 10 * self._value

    @ten_value.setter                                # Decorators for setter
    def ten_value(self , new_value):                 # Setter method
        self._value = new_value / 10
        
    def show(self):                                  # Default constructor
        print(f"Value is {self._value}")    


obj = MyClass1(10)
print("Initial ten_value:", obj.ten_value)           # Call getter:- Output: 100

obj.ten_value = 67                                   # Call setter
print("After setter:", obj.ten_value)                # Output: 67.0
obj.show()                                           # Output: Value is 6.7