a, b = 100, 100
for i in range(int(input())):
    x, y = map(int,input().split())
    if x > y:
        b -= x
    elif x < y:
        a -= y
    else:
        continue
print(a)
print(b)