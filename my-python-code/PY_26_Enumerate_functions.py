# Demonstrates the enumerate function for iterating with indices

# Define a list of marks
marks = [12 , 56 , 89 ,  55 , 96 , 99 ,84]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 5):
#         print("Saksham , Awesome!")
#     index += 1    


# # In short form:
# for index, mark in enumerate(marks):     
#     print(mark)
#     if(index == 5):
#         print("Saksham , Awesome!")



# Iterate with enumerate, starting index at 1
for index, mark in enumerate(marks, start=1):
    print(f"Mark {index}: {mark}")
    if index == 5:
        print("Saksham, Awesome!")