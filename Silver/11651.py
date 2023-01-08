import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    x, y = map(int,input().split())
    arr.append([y, x])

s_arr = sorted(arr)

for y, x in s_arr:
    print(x, y)