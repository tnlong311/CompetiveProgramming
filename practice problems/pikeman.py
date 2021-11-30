exCount, length = map(int,input().split())
inList = [int(i) for i in input().split()]

timeList = [inList[-1]]

for i in range(exCount-1):
    last = timeList[-1]
    new = (inList[0]*last+inList[1])%inList[2] +1
    timeList.append(new)

timeList.sort()

maxi=0
penalty=0
count=0
for i in timeList:
    maxi+=i
    penalty+=maxi
    if maxi > length:
        penalty+=-maxi
        break
    else:
        count+=1
penalty=penalty%1000000007    
print(count,penalty)