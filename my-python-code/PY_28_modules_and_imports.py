# Demonstrates importing modules and creating custom modules in Python

# import all math function/property
import math                        
a = math.floor(4.634)
a = math.sqrt(9)
print(a)


# Import specific functions from math
from math import sqrt, pi
result = sqrt(9) * pi
print("Square root of 9 * pi:", result)                           # Output :-> 9.42477796076938


# NOTE: Importing everything from the Math module can sometimes cause issues in the program.
# It's not recommended. Instead, import only the specific functions you need.

# from math import *
# result = sqrt(9) * pi
# print(result)                                                   # Output :-> 9.42477796076938
  

# Import with alias
from math import pi , sqrt as s        
result = s(9) * pi
print(result)                                                     # Output :-> 9.42477796076938

import math as m
result = m.sqrt(9) * m.pi
print("Using alias:", result)                                     # Output :-> 9.42477796076938


# List all attributes of a module
import math
print("Math module attributes:", dir(math))
print("Math.nan:", math.nan, "Type:", type(math.nan))



# Import custom module (assumes Saksham.py exists with welcome() function and saksham variable of String type)

# Example 1:
from Saksham import welcome, saksham
welcome()
print("Saksham variable:", saksham)

# Example 2:
from Saksham import *
welcome()
print("Saksham variable:", saksham)

# Example 3:
import Saksham as sak
sak.welcome()
print("Saksham variable:", sak.saksham)