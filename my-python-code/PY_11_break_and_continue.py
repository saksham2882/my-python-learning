# break, continue, and simulating a do-while loop in Python

# Break: Exits the loop entirely
for i in range(12):
    if i == 10:
        break
    print(f"5 X {i + 1} = {5 * (i + 1)}")
print("Exiting the loop")


# Continue: Skips the current iteration and continues with the next
for i in range(1, 12):
    if i == 10:
        print("Skip the iteration")
        continue
    print(f"5 X {i} = {5 * i}")


# Simulate do-while loop: Executes at least once
i = 0
while True:            # Infinite loop
    print(i)
    i += 1
    if i % 50 == 0:    # Break condition
        break