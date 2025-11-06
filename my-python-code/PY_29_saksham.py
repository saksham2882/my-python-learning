# Demonstrates the __name__ == "__main__" idiom to control code execution

def welcome():
    print("Hey You Are Welcome From Saksham")

# Print the module name (for understanding)
print("Module name:", __name__)


# Only run if this is the main module, not when imported
if __name__ == "__main__":
    welcome()

# Note: Using __name__ == "__main__" prevents code from running when this file is imported as a module, check the example in file -> PY_29_if_name__main