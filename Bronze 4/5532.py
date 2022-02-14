L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

res1 = 0
res2 = 0
res3 = 0
if A % C != 0:
    res1 += (A // C) + 1
else:
    res1 += A // C


if B % D != 0:
    res2 += (B // D) + 1
else:
    res2 += B // D


if res1 > res2:
    res3 += res1
else:
    res3 += res2

print(L - res3)