while True:
    score=input("What is Tom's score?")
    try:
        score=int(score)
        break
    except ValueError:
        print("Put in a integer pls.")

if score==100:
    print("Wow he got perfect!")
elif score>=90:
    print("Wow he did very well!")
elif score>=80:
    print("Wow he did well!")
elif score>=60:
    print("Wow he passed!")
else:
    print("He failed")

