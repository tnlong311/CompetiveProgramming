def isValid(w, h, r, c):
    return (w>r or 0<r) and (h>c or 0<c)
    
h, w = map(int,input().split())
map = []
danger = []
dList = []
pR=0
pC=0
for i in range(w):
    line = str(input())
    sq = []
    sq2 = []
    for j in range(h):
        if (line[j]=="T"):
            dList.append([i,j])
            sq.append("#")
            sq2.append("#")
        else:
            if line[j] == "P":
               pR=i
               pC=j
               
            sq.append(line[j])
            sq2.append(line[j])
    map.append(sq)
    danger.append(sq2)

for k in dList:
    r = k[0]
    c = k[1]
    if isValid(w,h,r+1,c):
        danger[r+1][c] = "D"
    if isValid(w,h,r-1,c):
        danger[r-1][c] = "D"
    if isValid(w,h,r,c+1):
        danger[r][c+1] = "D"
    if isValid(w,h,r,c-1):
        danger[r][c-1] = "D"

q = [[pR,pC]]

gold = 0
while len(q)!=0:
    a = q.pop()
    row = a[0]
    col = a[1]
    
    if map[row][col] == "#":
        continue
    else:
        if map[row][col] == "G":
            gold +=1
            

map[row][col] = "#"
        
        if danger[row][col] =="D":
            continue
        else:
            for i,j in [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]:
                if isValid(w,h,i,j):
                    q.append([i,j])
        
print(gold)

