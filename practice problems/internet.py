setList=[set({1})]

houses, cables = map(int,input().split())

unConnected=[i+1 for i in range(houses)]
for i in range(cables):
    first, second = map(int,input().split())
    
    firstPos=-1
    secondPos=-1
    
    for position in range(len(setList)):
        if first in setList[position]:
            firstPos=position
        if second in setList[position]:
            secondPos=position
    
    if firstPos == secondPos:
        if firstPos==-1:
            setList.append(set((first,second)))
    elif firstPos==-1:
        setList[secondPos].add(first)
    elif secondPos==-1:
        setList[firstPos].add(second)
    elif firstPos < secondPos:
        setList[firstPos].update(setList[secondPos])
        setList.remove(setList[secondPos])
    else: 
        setList[secondPos].update(setList[firstPos])
        setList.remove(setList[firstPos])
#     
#     aCheck=True
#     for eachSet in setList:
#         if first in eachSet and second in eachSet:
#             aCheck=False
#             break
#         elif first in eachSet:
#             check=True
#             aCheck=False
#             for nextSet in setList:
#                 if second in nextSet:
#                     eachSet.update(nextSet)
#                     setList.remove(nextSet)
#                     check=False
#                     break
#             if check:
#                 eachSet.add(second)
#             break
#         
#         elif second in eachSet:
#             aCheck=False
#             check=True
#             for nextSet in setList:
#                 if first in nextSet:
#                     eachSet.update(nextSet)
#                     setList.remove(nextSet)
#                     check=False
#                     break
#             if check:
#                 eachSet.add(first)
#             break
#     if aCheck:
#         setList.append(set((first,second)))
        
if len(setList) == 1:
    print('Connected')
else:
    for i in setList[0]:
        unConnected.remove(i)
    print(*unConnected,sep='\n')
    