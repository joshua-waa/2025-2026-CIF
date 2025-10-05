import random
g=input("Guess a number from 1-5")
n=random.randint(1,5)
if g==n:
    print("You got it correct!!")
else:
    print("You got it wrong, the correct number was",n,".")
