# Demonstrates class inheritance in Python


# Inheritance allows one class (child/subclass) to use the properties and methods of another class (parent/superclass).
# It helps in code reusability and creating a logical relationship between classes.


# Example 1:
# --------- Parent Class ---------
class Employee:
    def __init__(self , name ,id):
        self.name = name
        self.id = id

    def showDetails(self):    
        print(f"The name of Employee is {self.name} And Its Id is {self.id}  ")

# -------- Child Class -----------
# This is Inheritance. It means I created a class named 'Programmer' that has everything from the 'Employee' class, plus anything new that I add inside the 'Programmer' class.
class programmer(Employee):                             
    def showLanguage(self):
        print("The Default language is Python")
    

e1 = Employee("Rohit", 45)        
e1.showDetails()

e2 = programmer("Shivam", 7)        
e2.showDetails()
e2.showLanguage()




# Example 2:
# We can create any number  of Inheritance:-
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("Default language: Python")

class YouTuber(Programmer):
    def showChannel(self):
        print(f"{self.name} is a successful YouTuber")


e1 = Employee("Rohit", 45)
e1.showDetails()                                             # Output: Name: Rohit, ID: 45

e2 = Programmer("Shivam", 7)
e2.showDetails()                                             # Output: Name: Shivam, ID: 7
e2.showLanguage()                                            # Output: Default language: Python

e3 = YouTuber("XYZ", 69)
e3.showDetails()                                             # Output: Name: XYZ, ID: 69
e3.showChannel()                                             # Output: XYZ is a successful YouTuber