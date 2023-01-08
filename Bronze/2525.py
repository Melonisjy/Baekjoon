h, m = map(int,input().split())
time = int(input())

h += time // 60
m += time % 60
print(h)
print(m)

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)

