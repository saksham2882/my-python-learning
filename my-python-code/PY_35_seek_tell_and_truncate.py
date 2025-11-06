# Demonstrates seek(), tell(), and truncate() in file handling


# Seek() :- seek means to start counting after the given value and move the file pointer forward by that number of bytes.
# You can print after that if you want.

# tell() :- This tells us how far we have moved using seek().
# In other words, it shows our current position in the file (how many characters ahead we are).


# --- seek() and tell() ---
with open('PY_35_seek_and_tell.txt', 'r') as f:
    f.seek(10)                                        # Move cursor to 10th byte
    print("Current position:", f.tell())              # Output: 10
    data = f.read(5)                                  # Read next 5 characters
    print("Data read:", data)                         # Output: ABCDE



# --- truncate() ---
with open('PY_35_truncate_function.txt', 'w') as f:
    f.write('Hello Samsung_World_2')
    f.truncate(9)                                     # Keep only first 9 characters

with open('PY_35_truncate_function.txt', 'r') as f:
    content = f.read()
    print("After truncate:", content)                 # Output: Hello Sam
