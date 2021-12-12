#A game of rock, paper, scissors
#Using while loops and if/elif/else logic statements

import random
from ascii_art import graphics
from clearscreen import clear

play_again = True

#Loops through game if player wants to play again
while play_again:
  #Prompts user for input and prints out their choice
  player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print("You chose:")

  #Checks for invlaid input
  if player_choice >= 3 or player_choice < 0:
    print("Invalid number. You lose!")
  else:
    print(graphics[player_choice])

    #Chooses a random value for computer and prints out its choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(graphics[computer_choice])

    #Compares the user's and the computer's choice to determine the winner or whether it is a draw
    if player_choice == 0 and computer_choice == 2:
      print("You win!")
    elif player_choice == 2 and computer_choice == 0:
      print("You lose!")
    elif player_choice > computer_choice:
      print("You win!")
    elif player_choice < computer_choice:
      print("You lose!")
    elif player_choice == computer_choice:
      print("It's a draw!")

  #Checks to see if player wants to play again or not
  play_option = input("Would you like to play again? Type Y or N ").upper()
  if play_option == "N":
    play_again = False
    print("\nThanks for playing!")
  else:
    clear()
