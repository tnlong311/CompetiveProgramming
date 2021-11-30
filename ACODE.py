while True:
    i = str(input())
    if (int(i)==0):
        break
    
    num = [1,1]
    
    k = 1
    while k < len(i):
        if ((i[k-1] == "1" or (int(i[k]) <= 6 and i[k-1] == "2")) and (int(i[k]) > 0)):      
            a= num[-1]+num[-2]
            num.append(a)
        else:
            num.append(num[-1])
            
            
        k+=1
    
#     print(num)
    print(num[-1])