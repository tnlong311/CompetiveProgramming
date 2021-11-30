word = str(input())
result = word[0]
for i in range(1,len(word)):
    if word[i] != result[-1]:
        result += word[i]
        
print(result)
    