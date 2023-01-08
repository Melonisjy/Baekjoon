n = int(input())
arr = []

for i in range(n):
    x, y = map(int,input().split())
    arr.append((x, y))

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')