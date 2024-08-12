import random
def rpc(self):
    user_input = input("Rock, Paper, Scissor say shoot: ").lower()
    select = ["rock", "paper", "scissors"]
    Computer = random.choice(select)
    if user_input == Computer:
        print("It's a tie")
        rpc()
    elif Computer == "rock" and user_input == "paper":
        print("Paper beats Rock, you WIN!!!")
    elif Computer == "paper" and user_input == "scissors":
        print("Scissors beats Paper, you WIN!!!")
    elif Computer == "scissors" and user_input == "rock":
        print("Rock beats Scissors, you WIN!!!")
    else:
        print("You lost")
        rpc()  
rpc()