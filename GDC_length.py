n = int(input())
for i in range(n): 
    a,b,c = map(int, input().split())

    if (a==b and b==c):
        x = 2*pow(10,a-1)
        y = 3*pow(10,b-1)
    elif (a>b):
        x = pow(10,a-1)+pow(10,c-1)
        y = pow(10,b-1)
    else:
        x = pow(10,a-1)
        y = pow(10,b-1)+pow(10,c-1)
          
    print(x, y)
