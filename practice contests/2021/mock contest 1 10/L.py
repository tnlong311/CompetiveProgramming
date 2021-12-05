n = int(input())
w = str(input())
sad = 0
happy = 0
    
for i in range(n-1):
    n1 = w[i]
    n2 = w[i+1]
    
    if n1 == ":":
        if n2 =="(":
            sad += 1
        elif n2 == ")":
            happy += 1
    elif n2 == ":":
        if n1 ==")":
            sad += 1
        elif n1 == "(":
            happy += 1

                
if (sad > happy):
    print("SAD")
elif sad == happy:
    print("BORED")
else:
    print("HAPPY")