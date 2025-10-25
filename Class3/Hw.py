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
n=random.randint(a,b)
y="y"
lives = 3
while True:
    while y == "y":
        g=input(f"Guess a number from { a } - { b } .")
        try:
            g=int(g)
            break
        except ValueError:
            print("Put a integer")

    if g==n:
        print("You got it correct!!")
        break
    else:
        print("You got it wrong.")
        lives -= 1
        print(f"You have: {lives} lives left.")
        if lives ==0:
            print("You dont have enough lives left!")
            break

        if n >= g:
            print("Too small.")
        else:
            print("Too big.")
        y=input("Do yo you want to try again(y/n)?")
