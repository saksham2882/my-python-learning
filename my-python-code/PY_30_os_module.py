# Demonstrates file system operations using the os module

import os

# Create a directory if it doesn't exist
if not os.path.exists("data"):
    os.mkdir("data")


# Create multiple directories
try:
    for i in range(1, 10):
        os.mkdir(f"data/Day{i}")
except FileExistsError:
    print("Directories already exist")


# Rename directories
for i in range(1, 10):
    if os.path.exists(f"data/Day{i}"):
        os.rename(f"data/Day{i}", f"data/Tutorial{i}")


# List directories and their contents
folders = os.listdir("data")
print("Folders in data:", folders)

for folder in folders:
    print(f"Contents of {folder}:", os.listdir(f"data/{folder}"))


# Get current working directory
print("Current working directory:", os.getcwd())