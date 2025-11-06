# Introduction to Object-Oriented Programming (OOP)


# Class: Blueprint for creating objects
class RailwayForm:
    formType = "Railway Reservation"

    def printData(self):
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")


# Objects: Instances of the class
saksham = RailwayForm()
saksham.name = "Saksham"
saksham.train = "Rajdhani Express"
saksham.printData()


# Output:
# Name: Saksham
# Train: Rajdhani Express
