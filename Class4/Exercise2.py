def ifdivisible(num1, num2):
    if num1%num2==0:
        answer="True"
    else:
        answer="False"

    return answer
a=int(input("First number?"))
b=int(input("Second number?"))
print(ifdivisible(a,b))
