# Demonstrates classes, objects, and the 'self' parameter

class Person:
    name = "Rohit"
    occupation = "Software Developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

# Create objects
a = Person()
a.info()                                                 # Output: Rohit is a Software Developer


a.name = "Shubham"
a.occupation = "Student"
a.info()                                                 # Output: Shubham is a Student     # This is a self call          



# self: It is a reference to the current instance of the class and is used to access variables that belong to that class.
# self means the object for which the method is being called.
# For example, when we call b.info(), the 'self' inside the class will refer to 'b'.
# If 'b' represents Shivam, then 'self' will contain Shivam's details (like name, occupation, etc.).
# In short, it tells the code to run or return results for the specific data (object) we are passing.


b = Person()                                            # This is a object  
b.name = "Shivam"           
b.Occupation = "HR"
b.info()                                                # self call (name , occupation used)

# NOTE: In Python, the self argument is a convention used in object-oriented programming to refer to the instance of the class. It allows access to the attributes and methods of the class in Python. When defining methods for a class, self is used as the first parameter in each case.