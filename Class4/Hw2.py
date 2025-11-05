weather=[
    ["Monday", [20,11,5,"sunny"]],
    ["Tuesday", [17,15,2,"cloudy"]],
    ["Wednesday", [13, 8, 7, "rain"]],
    ["Thursday", [11, 5, 6, "sunny"]],
    ["Friday", [16, 15, 1,"sunny"]],
    ["Saturday", [19, 15, 3, "sunny"]],
    ["Sunday", [17, 15, 2, "rain"]],
]
a=0
for i in weather:
    print(f"On {weather[a][0]} the highest temperature is {weather[a][1][0]} and the lowest temperature is {weather[a][1][1]}. The wind speed is {weather[a][1][2]}kmph.It is going to be {weather[a][1][3]}")
    a+=1
