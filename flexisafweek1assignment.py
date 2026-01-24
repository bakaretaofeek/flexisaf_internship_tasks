# create a game of rock, paper and scissors between the user and the computer. 
# The program must define the possible choices, get the user's choice, 
# generate a random choice for the computer, 
# determine the winner based on the rules of rock, paper and scissors
import random
print('This is a game of rock, paper and scissors... You can only input one of rock, paper or scissors')
# These are the options for the computer to choose from
choices = ['rock', 'paper', 'scissors']
print(choices)
# collecting the choice of user
user_choice = input('what is your choice: ').lower()
# the computer randomly selects any of the three options in choices
computer_choice = random.choice(choices)
# this is to ensure the integrity of the inputs... any other word aside from the options in choices is void
if user_choice not in choices:
    print('Invalid input... stick to the game options!')
else:
    print('You chose: ',user_choice)
    print('Computer chose: ', computer_choice)
    
    if user_choice == computer_choice:
        print('It is a tie')
    elif ((user_choice == 'paper' and computer_choice == 'rock') or
          (user_choice == 'scissors' and computer_choice == 'paper') or
          (user_choice == 'rock' and computer_choice == 'scissors')
          ):
        print('You Win')
    else:
        print('Computer Wins')
    



