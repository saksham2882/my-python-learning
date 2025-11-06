# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# Coding:
# if the word contains at least 3 characters , remove the first letter and append it at the end.
# now append three random characters at the starting and the end
# else: simply reverse the string

# Decoding:
# if the word contains less then 3 characters , reverse it
# else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.
# Your Program should ask whether you want to code or decode



try:
    # Get user input
    String = input("Enter Your Secret Message here: ")
    words = String.split(" ")
    coding = input("1 for Coding or 0 for Decoding: ")
    coding = True if (coding == "1") else False
    
    # Encoding
    if(coding):
        new_word = []
        for word in words:
            if(len(word)>=3):
                random1 = "dcv"
                random2 = "wef"
                String_new = random1 + word[1:] + word[0] + random2
                new_word.append(String_new)
            else:
                new_word.append(word[::-1])    
        print("Coded message:", " ".join(new_word))        
    
    # Decoding 
    else:
        new_word = []
        for word in words:
            if(len(word)>=3):
                String_new = word[3:-3]
                String_new = String_new[-1] + String_new[:-1]
                new_word.append(String_new)
            else:
                new_word.append(word[::-1])    
        print("Decoded message:", " ".join(new_word))
                                
except ValueError:
    print("Error: Invalid input")