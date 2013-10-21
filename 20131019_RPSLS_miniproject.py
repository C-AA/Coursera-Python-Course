# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "Unrecognized"
    return name

    
def name_to_number(name):
   if name == "rock":
        number = 0
   elif name == "Spock":
        number = 1
   elif name == "paper":
        number = 2
   elif name == "lizard":
        number = 3
   elif name == "scissors":
        number = 4
   else:
        number = 5
   return number
        
def rpsls(player_guess): 
    # fill in your code below
    print "Player chooses", player_guess
    # convert name to player_number using name_to_number
    p_guess = name_to_number(player_guess)
    # compute random guess for comp_number using random.randrange()
    comp_number = int(random.randrange(0,5))
    # compute difference of player_number and comp_number modulo five
    result = p_guess - comp_number
    # use if/elif/else to determine winner
    if (p_guess - comp_number) % 5 == 1 or (p_guess - comp_number) % 5 == 2:
        winner = "Player"
    elif (p_guess - comp_number) % 5 == 3 or (p_guess - comp_number) % 5 == 4:
        winner = "Computer"
    elif (p_guess - comp_number == 0):
        winner = "Tie" 
    else:
        winner = "Impossible!"
    # convert comp_number to name using number_to_name
    print "Computer chooses", number_to_name(comp_number)
    
    # print results
    if winner == "Tie":
        print "Player and Computer tie!\n"
    else:
        print winner, "wins.\n"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
##
# print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)
#print number_to_name(5)
#print name_to_number("rock")
#print name_to_number("Spock")
#print name_to_number("paper")
#print name_to_number("lizard")
#print name_to_number("scissors") 
