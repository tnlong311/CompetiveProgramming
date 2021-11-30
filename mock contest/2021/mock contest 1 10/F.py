n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    print(1/l - 1/(r+1))