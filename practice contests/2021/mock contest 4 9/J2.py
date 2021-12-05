fact =[1,1]
for i in range(2,2501):
    fact.append(i*fact[-1])
    
print(fact)