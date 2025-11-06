# Demonstrates Python's naming conventions for public, private, and protected members.

# Python does **not** enforce access control – it is purely conventional.
# In Python, there is no strict concept of public, private, or protected like in other languages.

# Public Access Modifiers       :- Access from outside the class also (any where)
# Private Access Modifiers      :- Not Access from outside the class (function)
# Protected Access Modifiers    :- Access Only from the inside of class and subclass. 

# All the variables and methods in python are by default 'public' access modifier.



# ------------ Public Access Modifier -------------
class EmployeePublic:
    def __init__(self):
        self.name = "Ram"                             # Public attribute

a = EmployeePublic()
print(a.name)                                         # Output: Ram



# ------------ Private Access Modifiers (Name Mangling) -------------
# Using "__" before a variable name indicates that it is private.
# However, it can still be accessed using (_ClassName__variable).

class Employee:
    def __init__(self):
        self.__name = "Kim"

a = Employee()        
# print(a.__name)                                    # AttributeError – direct access blocked
print(a._Employee__name)                             # Can be accessed directly.


# Now the question is, why are we able to access it?
# The answer is: because of "Name Mangling".
# Name Mangling means that Python internally changes the name of a private attribute to include the class name, making it harder (but not impossible) to access directly.



# ----------- Protected Access Modifiers -------------
class Student:
    def __init__(self):
        self._name = "Rohit"                         # Protected attribute (by convention)

    def _funName(self):                              # Protected method
        return "Rohit is a Good Boy"

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# Access from Student instance
print(obj._name)                                     # Output: Rohit
print(obj._funName())                                # Output: Rohit is a Good Boy

# Access from Subclass instance
print(obj1._name)                                    # Output: Rohit
print(obj1._funName())                               # Output: Rohit is a Good Boy



# NOTE:- In Python, it's not fixed that "_" makes a variable protected and "__" makes it private.
# These are just naming conventions that developers follow.
# Python doesn’t enforce any strict access rules.
# However, when "__" is used, Python performs name mangling,
# which means the variable cannot be accessed directly.
# If only "_" is used, it can still be accessed directly.
