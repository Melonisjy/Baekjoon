n = int(input())

arr = list(map(str,input()))
a = 0
b = 0
for i in range(0, n):
    if arr[i] == 'A':
        a += 1
    elif arr[i] == 'B':
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')