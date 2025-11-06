# Demonstrates constructors in Python classes


# Previous file (without use of constructors.)
class person:
    name = "Rohit"
    occ = "Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

# create object 
a = person()
# a.name = "Shivam"
# a.occ = "HR"
a.info()                                                              # Output: Rohit is a Developer



# Constructor:-
class person:
    def __init__(self):                                               # This is a default constructor.
        print("Hey I'm a good person")

b = person()                                                          # Output: Hey I'm a good person
c = person()                                                          # Output: Hey I'm a good person

# NOTE:    
# It means the constructor is called every time we create an object.
# So, each time an object is created, the constructor function will be executed.
       


# Now we pass the argument:-
class Person:
    def __init__(self, name, occ):                                    # This function will always return None.  This is a parameterized constructor (which means it contains parameters). 
        print("Constructor called!")
        self.name = name
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")


# Objects trigger constructor automatically
a = Person("Rohit", "Developer")                                      # Output: Constructor called!
b = Person("Shivam", "HR")                                            # Output: Constructor called!

# NOTE: # There might be some confusion here because the function takes three arguments, but we are passing only two while creating the object. This happens because 'self' is automatically passed as the first argument.

# c = person(1,2,3)                                                   # It show an error because aur function is take only two argument. one "self" is a automatic argument.

a.info()                                                              # Output: Rohit is a Developer
b.info()                                                              # Output: Shivam is a HR