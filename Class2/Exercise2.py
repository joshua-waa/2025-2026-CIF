stuff=["apple","banana","cherry",1,2,3]

for i in range(len(stuff)):
    print(stuff[i])

num=0
while True:
    if num<len(stuff):
        print(stuff[num])
        num+=1
    else:
        break

