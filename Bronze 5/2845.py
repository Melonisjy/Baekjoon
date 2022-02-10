a, b = map(int,input().split())
c = list(map(int,input().split()))

res = a * b

for i in c:
    print(i - res,end=' ')
