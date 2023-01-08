price = int(input())
n = int(input())
real=0

for i in range(n):
    a, b = map(int,input().split())
    real += a*b

if price == real:
    print("Yes")
else:
    print("No")