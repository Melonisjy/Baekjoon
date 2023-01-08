a, b, c, d, e = map(int,input().split())

f = a * a
g = b * b
h = c * c
i = d * d
j = e * e

result = f + g + h + i + j

res = result % 10

print(res)