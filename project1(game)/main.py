import random
'''

0 for rock
1 for paper
2 for scissors

'''

from typing import Dict



computer = random.choice([0,1,2])
youstr = input("What do you choose? Type 'r' for Rock, 'p' for Paper or 's' for Scissors.\n :")
youDict = {"r":0, "p":1, "s":2}
reverseDict = {0:"rock", 1:"paper", 2:"scissors"}
try:
  you = youDict[youstr]
except KeyError:
  print("Invalid input! Please enter 0, 1, or 2.")
  exit(1)
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("It's a draw")

else:
    if (computer == 2 and you==0):
      print("You win") 

    elif (computer == 2 and you == 1 ):
      print("You lose")

    elif (computer == 0 and you == 2 ):
      print("You lose")

    elif (computer == 1 and you == 0 ):
      print("You lose")

    elif (computer == 1 and you == 2 ):
      print("You win")

    elif (computer ==0 and you == 1):
      print("You win")    

    else:
      print("something went wrong")