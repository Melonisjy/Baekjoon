days = int(input())

a, b, c, d, e = map(int,input().split())

count = 0

for i in range(1):
    if a == days:
        count += 1
    if b == days:
        count += 1
    if c == days:
        count += 1
    if d == days:
        count += 1
    if e == days:
        count += 1

print(count)


