from enum import Enum
import random

class Choice(Enum): 
    ROCK = 1
    PAPER = 2
    SCISSORS = 3 

print("Enter your choice where:\n 1-> 🪨  Rock \n 2-> 📄 Paper \n 3-> ✂️  Scissors")
player_input = int(input(" Enter your choice: "))

player_choice = Choice(player_input)
computer_random = random.randint(1, 3)
computer_choice = Choice(computer_random)

print(f"\nYou chose: {player_choice.name}")
print(f"Computer chose: {computer_choice.name}\n")

if player_choice == computer_choice:
    print("🤝 Tie!")
elif (player_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or \
     (player_choice == Choice.PAPER and computer_choice == Choice.ROCK) or \
     (player_choice == Choice.SCISSORS and computer_choice == Choice.PAPER):
    print("🎉 You Win!")
else:
    print("😢 Computer Wins!")