import random
q=["What is the initials of the first american president?(Eg: abraham lincon= al)",
   "What year is it?",
   "Name the most popular ice-cream flavour.",
   "What is (9+6)/3?",
   "Name the largest web browser.",
   "What is the value of π (two decimals)?",
   "What do bees collect from flowers?",
   "What is the largest ocean on Earth?(one word)",
   "What’s H₂O commonly called?"]
a=["gw",
   "2025",
   "vanilla",
   "5",
   "chrome",
   "3.14",
   "nectar",
   "pacific",
   "water"]
lives=int(3)
al=[]
hq=[1,4,6,7,9]
def intro():
    print("Welcome to a TBAG game.")
    print("Here are the instructions")
    print("1.Only use lower-case letters\n2.Only type things to answer the question, no unnecessary words or spaces.\n3.You only have 3 lives.\n4.Some harder questions will give you 1 life.\n5.Have fun!\nQuestion time!")
intro()
for i in range(len(q)):
    again=1
    while again==1:
        n=random.randint(0,len(q)-1)
        if n in al:
            again=1
        else:
            again=0
        al.append(n)
    answer=input(q[n])
    if answer==a[n]:
        print("You got it correct!")
        if (n+1) in hq:
            lives+=1
            print("You got an extra life!!")
        print(f"You have {lives} lives left.")
    else:
        lives -=1
        print("You got it wrong.")
        print(f"The correct answer is {a[n]}.")
        print(f"You have {lives} lives left.")

    if lives==0:
        print("You ran out of lives!")
        break
print("You finished the game!")
