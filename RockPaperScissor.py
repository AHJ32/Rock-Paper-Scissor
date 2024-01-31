import random


def logic(user):
    game = ["R", "P","S"]
    # Rock > Scissor
    # Scissor > Paper
    # Paper > Rock
    ai = random.choice(game)
    
    
    if user == ai:
        print("Its a draw")
    elif user == "R" and ai == "S" or user == "S" and ai == "P" or user == "P" and ai == "R":
        print("You win ")
    elif user == "S" and ai == "R" or user == "P" and ai == "S"or user == "R" and ai == "P":
        print("You loose ")
        
user = str(input("\tR = Rock\tP = Paper\tS = Scissor\n=>"))

if user == "R" or user == "P" or user == "S":
    print(f"You have choosen {user}")
    logic(user)
else:
    print("Invalid Input")
    