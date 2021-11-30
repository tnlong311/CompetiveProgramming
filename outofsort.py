n,m,a,c,x0 = map(int, input().split())
lst = [x0]
for i in range(n):
    lst.append((a*lst[i]+c)%m)
# print(lst[1:])
def bisearch(lst, v, left, right):
    if (left > right):
        return False
    
    mid = int((left+right)/2)
    
#     print("value:",v)
#     print("left: %d, right: %d, mid: %d" %(left,right,mid))
#     print("value mid:",lst[mid])
    if (lst[mid] == v):
#         print(v)
#         print("taken")
        return True
    elif (lst[mid] < v):
        return bisearch(lst,v,mid+1,right)
    else:
        return bisearch(lst,v,left,mid-1)

count = 0

lst2 = lst[1:]
l = len(lst2)-1
# print(lst2)
for i in range(n):
    v = lst2[i]
    if bisearch(lst2,v,0,l):
        count +=1

print(count)
    
# print(bisearch([6,1,4,7,2,1],4,0,6))