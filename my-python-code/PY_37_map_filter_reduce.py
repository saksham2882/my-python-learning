# Demonstrates map, filter, and reduce - higher-order functions


numbers = [1, 3, 4, 9, 6, 2, 8]


# --- map: Apply function to each item ---
cubes = list(map(lambda x: x**3, numbers))
print("Cubes:", cubes)                                         # Output: [1, 27, 64, 729, 216, 8, 512]


# --- filter: Keep items where function returns True ---
greater_than_4 = list(filter(lambda x: x > 4, numbers))
print("Greater than 4:", greater_than_4)                       # Output: [9, 6, 8]


# NOTE: 
# The filter function returns True or False for each item in list1 (an iterable).
# It checks every element and stores only the filtered ones in new_list1.


# --- reduce: Reduce list to single value ---

# The reduce function must always be imported before using it.
from functools import reduce

sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum_all)                                         # Output: 33


# how reduce implement: let Number = [1,2,3,4,5] 
# number = [1,2,3,4,5]
# number = [3,3,4,5]                                           # we adding because which function we call it is add of two number 
# number = [6,4,5] 
# number = [10,5] 
# number = [15]                                                # Output: 15