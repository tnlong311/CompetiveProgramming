n, m = map(int, input().split())

graph =[]
printList = []
for i in range(n):
    graph.append([])
    printList.append(1)
    
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
minLen = n
minP = 0
for j in range(n):
    if len(graph[j]) < minLen:
        minLen = len(graph[j])
        minP = j
        
printList[minP] = 0
for k in graph[minP]:
    printList[k] = 0
    
for p in range(0,n-1):
    print(printList[p], end=" ")

print(printList[-1])
