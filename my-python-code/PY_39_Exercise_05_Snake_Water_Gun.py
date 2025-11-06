# Snake-Water-Gun:

# Snake, Water and Gun is a Variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake , water , or a gun. The gun beats the snake , the water beats the gun, and the snake beats the water.
# Write a python program to create a snake water gun game in python using if-else statements. Do not create any fancy GUI. Use proper Functions to check for win.  


import random

def check_win(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 's' and computer == 'w') or \
         (player == 'w' and computer == 'g') or \
         (player == 'g' and computer == 's'):
        return "You win!"
    else:
        return "You lose!"

choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
print("Snake-Water-Gun Game")
print("s = Snake, w = Water, g = Gun")

player = input("Your choice (s/w/g): ").lower()

if player not in choices:
    print("Invalid choice!")
else:
    computer = random.choice(['s', 'w', 'g'])
    print(f"You: {choices[player]}")
    print(f"Computer: {choices[computer]}")
    print(check_win(player, computer))


# Sample Output:
# You: Snake
# Computer: Water
# You win!