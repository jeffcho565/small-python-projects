import random
class randomGuess:
    def game():
        count=0
        ans= random.randint(1,100)
        while count in range(0,10):
            count+=1
            guess=int(input("what is your guess between 1-99:"))
            if guess>ans:
                sum=guess-ans
                print("Your answer was Higher than the answer")
            elif guess<ans:
                print("Your answer was Lower than the answer")
            else:
                print("You got it, the answer was %d"%(ans))
    game()