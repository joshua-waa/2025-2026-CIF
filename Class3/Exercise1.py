import random
while True:
    a=input("What lower bound of your guessing game?")
    try:
        a = int(a)
        break
    except ValueError:
        print("Put a integer")
while True:
    b = input("What upper bound of your guessing game?")
    try:
        b = int(b)
        break
    except ValueError:
        print("Put a integer")
while True:
    g=input(f"Guess a number from { a } - { b } .")
    try:
        g=int(g)
        break
    except ValueError:
        print("Put a integer")
n=random.randint(a,b)
if g==n:
    print("You got it correct!!")
else:
    print("You got it wrong, the correct number was",n,".")
