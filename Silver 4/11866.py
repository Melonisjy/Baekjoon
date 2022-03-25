from collections import deque

n, k = map(int,input().split())

arr = list(range(1, n+1))
arr = deque(arr)
print("<", end='')


while(arr):
    for i in range(k-1):
        arr.append(arr.popleft())
    print(arr.popleft(), end='')

    if arr:
        print(", ", end='')

print(">")
