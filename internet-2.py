houses, cables = map(int,input().split())

visited = []
connections = []
for i in range(houses):
    visited.append(False)
    connections.append([])

for i in range(cables):
    first, second = map(int,input().split())
    connections[first-1].append(second-1)
    connections[second-1].append(first-1)
    
check = []
check.extend(connections[0])

while len(check)!=0:
    house = check.pop()
    if not visited[house]:
        visited[house] = True
        for i in range(len(connections[house])):
            if not visited[connections[house][i]]:
                check.append(connections[house][i])
        
#     check.remove(check[0])

final = True
for i in range(1,len(visited)):
    if not visited[i]:
        final=False
        print(i+1)
        
if final:
    print('Connected')
        
    