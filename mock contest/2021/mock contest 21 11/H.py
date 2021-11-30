n, m, d = map(int, input().split())

train = []

for i in range(n):
    train.append(str(input()))

print(train)

for i in range(m):
    test = str(input())
    
    if test in train:
        print(test)
        print("BAD")
    else:
        print("GOOD")