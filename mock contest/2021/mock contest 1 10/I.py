import math

r,R,h = map(int, input().split())

c = math.atan(h/(R-r))
x = math.tan(c/2)*(R)

if x > h/2:
    print(h/2)
else:
    print(x)


