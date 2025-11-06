# Demonstrates reading lines and writing multiple lines using readline() and writelines()
 

# -------- Readline line by line ------------
f = open('PY_Sample_read_readline.txt' , 'r') 
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# This line are for above code. If want to run this code move it to the .txt file then run
# Hello Friends , What's up.
# This is a good code.
# Today is a 13/12/2023


# Example:
# --- Reading line by line  and parsing student marks ---
with open('read_readline.txt', 'r') as f:
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        
        # Split line into marks (as strings)
        marks = line.strip().split(',')
        if len(marks) == 3:
            m1 = int(marks[0])
            m2 = int(marks[1])
            m3 = int(marks[2])
            print(f"Student {i} - Math: {m1*2}, English: {m2*2}, Hindi: {m3*2}")
        i += 1

# Output:
# Student 0 - Math: 112, English: 90, Hindi: 134
# Student 1 - Math: 24, English: 130, Hindi: 92



# --- Writing multiple lines at once ---
lines = ['line 1\n', 'line 2\n', 'line 3\n']
with open('PY_Sample_Writelines.txt', 'w') as f:
    f.writelines(lines)                                # If the file size is very large (for example, coming from a database), we should use f.write(lines) instead of f.writelines(lines).



# Output in PY_Sample_Writelines.txt:
# line 1
# line 2
# line 3
# 