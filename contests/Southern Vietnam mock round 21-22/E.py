i, j = map(int, input().split())
i = i/100  
if i == 1:
    print((j-j/6)*100)
else:
    m = (-8*i*j+7*j)/(12-12*i)

    if (m >= j/6) and (m <= j/3):
        print(((j-m)*(6*(1-i)*m/j+2*i-1))*100)      
    else:
        k = (j-j/3)*100
        p = (j-j/6)*i*100
        if k>p:
            print(k)
        else:
            print(p)
