print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


first_input = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if first_input == "left":
  second_input = input('You\'ve come to a lake. There is an island in the middle   of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  
  if second_input == "wait":
    third_input = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
    if third_input == "red":
      print('It\'s a room full of fire. Game Over.')
    elif third_input == "blue":
      print('You enter a room filled with vicious beasts. Game Over.')
    elif third_input == "yellow":
      print('You found the treasure! You win!')
    else:
      print("You chose a door that does not exist in this realm. Game Over.")
  else:
    print('You were attacked by Tyrannosaurus Troutus. Game Over.')
else:
  print("You fell into a hole. Game Over.")
