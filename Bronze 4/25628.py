a, b = map(int,input().split())
res = 0

while True:
    if a >= 2 and b >= 1:
        res += 1
        a -= 2
        b -= 1

    if a < 2 or b < 1:
        break
print(res)