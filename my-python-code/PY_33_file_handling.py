# Demonstrates file handling in Python for reading and writing

# # Modes in file
# 1. read(r)    : read the file
# 2. write(w)   : write in the file (if file not exist then it create a file )
# 3. append(a)  : open the file for appending only and create a new file if file does not exists
# 4. create(x)  : create a file and give an error if the file already exists.
# 5. text(t)    : It shows which file is open means "rt" :- means read this text file. If use "rb" then it means open file as a binary File.
# 6. binary(b)  : used to handle binary File(images, pdfs, etc.)


# READING A FILE

f = open('PY_33_file_handling.txt' , 'r')                # here 'r' for reading the file not the text inside of file
text = f.read()                                          # this for read the content inside the file.
print(text)
f.close() 


# Better way 
try:
    with open("PY_33_file_handling", "r") as f:           
        text = f.read()                                   
        print("File content:", text)
except FileNotFoundError:
    print("File not found")



# WRITING A FILE

f = open('PY_33_file_writing.txt' , 'w')
# f = open('PY_33_file_writing.txt' , 'a')                # If use append it add message every time in file if we run the program.   
f.write('Hello , World!')
f.close() 


# Shortcut "use of with"  so no use of Close() every time:-
# Note: Using 'with' automatically closes the file
with open('PY_33_file_writing.txt' , 'a') as f:
    f.write(" Hey I am inside 'with' ")
