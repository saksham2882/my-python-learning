# exception handling in Python

# Multiplication table with error handling
a = input("Enter the Number: ")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except ValueError:
    print("Invalid Input: Please enter a valid integer")



# Handle multiple exception types
try:
    num = int(input("Enter an integer: "))
    a = [6, 5]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")

print("Some important lines of code")
print("End of Program")



##################   finally clause in Python, which always executes    ###############

# Example 1:
try:
   l = [1 , 6 , 8 , 9]
   i = int(input("Enter the index: "))
   print(l[i])
except:
   print("Some error occurred")    

finally:
   print("I am Always executed")    


# Example 2:
def func1():
    try:
        l = [1, 6, 8, 9]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed, even after return")

# Call function and print return value
x = func1()
print("Return value:", x)



#############    raising and defining custom exceptions in Python     ##################

# Define a custom exception class
class CustomError(Exception):
    pass


# Example: Raise ValueError for invalid range using 'raise'
try:
    a = int(input("Enter a value between 5 and 9: "))
    if a < 5 or a > 9:
        raise ValueError("Value must be between 5 and 9")
    print("Valid input:", a)
except ValueError as e:
    print("Error:", e)


# Example: Custom exception for quitting
try:
    user_input = input("Enter 'quit' to exit: ")
    if user_input != "quit":
        raise CustomError("You must enter 'quit' to exit")
    print("Ok done, you quit")
except CustomError as e:
    print("Error:", e)