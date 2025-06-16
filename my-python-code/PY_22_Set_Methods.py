# set operations in Python

s1 = {1, 2, 3, 5, 6, "rahul", "rohit"}
s2 = {1, 5, 6, 8, 9, "saksham", "rohit"}

# Union: Combines all unique elements from both sets
print("Union:", s1.union(s2))


# Update: Adds elements from s2 to s1
s1_copy = s1.copy()  # Avoid modifying original
s1_copy.update(s2)
print("After update s1:", s1_copy)


# Intersection: Common elements in both sets
print("Intersection: ", s1.intersection(s2))


# Symmetric difference: Elements in either set, but not both  ( A symmetric difference B = (A-B) U (B-A) )
print("Symmetric difference:", s1.symmetric_difference(s2))


# Difference: Elements in s1 but not in s2
print("Difference:", s1.difference(s2))


# Disjoint: True if no common elements
A = {"Korea", "South Korea", "India"}
B = {"USA", "UK", "Seoul"}
print("Are A and B disjoint?", A.isdisjoint(B))


# Superset and subset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul" , "Kabul"}
cities3 = {"Tokyo", "Madrid", "Delhi"}
print("Is cities a superset of cities2?", cities.issuperset(cities2))
print("Is cities a superset of cities3? ", cities.issuperset(cities3))
print("Is cities3 a subset of cities? ", cities3.issubset(cities))


# Add elements
cities = {"Delhi", "Kanpur", "Berlin"}
cities.add("Madrid")
print("After add('Madrid'):", cities)


# Remove vs discard
# The main difference b/w the remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raises any error.
cities.remove("Berlin")
cities.discard("Berlin")
# cities.remove("Tokyo")                             # this show an error
cities.discard("Tokyo")                              # this does not show an error


# Pop: Removes and returns a last item (random item)
item = cities.pop()
print("Popped item:", item, "Remaining set:", cities)


# del: it is not a method , rather it is a keyword which deletes the set entirely.
# cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
del cities
# print(cities)                                      # It show an NameError 


# Clear: clears all items in the set and print an empty set.
cities2.clear()
print("After clear():", cities2)