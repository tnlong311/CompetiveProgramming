streets = int(input())
graph = []
reverseGraph = []
for i in range(1000):
    graph.append([])
    reverseGraph.append([])

printId = []
for no in range(streets):
    inList = [int(i) for i in input().split()]
    
    streetId = inList[0]
    printId.append(streetId)
    
    if inList[1] != 0:
        graph[inList[0]] = inList[2:]
        for i in inList[2:]:
            reverseGraph[i].append(streetId)

reached = [True]
reverseReached = [True]
for i in range(999):
    reached.append(False)
    reverseReached.append(False)

check = [0]
while len(check)>0:
    road = check.pop()
    
    for go in graph[road]:
        if not reached[go]:
            check.append(go)
            reached[go]=True

reverseCheck = [0]
while len(reverseCheck)>0:
    road = reverseCheck.pop()
    
    for go in reverseGraph[road]:
        if not reverseReached[go]:
            reverseCheck.append(go)
            reverseReached[go]=True
            
# print out answers
noProb = True
for i in printId:
    if not reverseReached[i]:
        print("TRAPPED",i)
        noProb = False

for i in printId:
    if not reached[i]:
        print("UNREACHABLE",i)
        noProb = False

if noProb:
    print("NO PROBLEMS")
    
    

