n = int(input())

arr = []
for i in str(n):
    arr.append(int(i))

arr.sort(reverse=True)

for i in arr:
    print(i, end='')
