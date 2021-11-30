n = int(input())
for i in range(n):
    k = int(input())
    
    f = 2
    check = True
    while k > 1:
        if k%f > 0:
            if f == 2:
                check = False
                break
            else:
                f = 2
        else:
            k = k/f
            f += 1
    
    if check:
        print('YES')
    else:
        print('NO')