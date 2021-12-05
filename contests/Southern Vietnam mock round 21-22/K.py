n = int(input())
pList = [int(i) for i in input().split()]
a = int(input())
s = int(input())

b = abs(a-s)
for i in range(n):
    pList[i] = abs(pList[i]-s)
    
pList.sort()

count = 0
j = 0
while b>0 and j<n:
    b = b-pList[j]
    if b>0:
        count+=1
        
    j += 1
    
print(count)
    