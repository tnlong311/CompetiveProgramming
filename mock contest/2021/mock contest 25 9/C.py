p = int(input())

result = []
for i in range(p):
    result.append(-1)

for i in range(p):
    result[(i*i) % p] = i

for j in range(p-1):
    print(result[j], end=" ")

print(result[-1], end="")