H, M, S = map(int,input().split())
time = int(input())

S += time
if S > 59:
    M += (S // 60)
    S = S % 60
    if M > 59:
        H += M // 60
        M = M % 60
        if H > 23:
            H = H % 24

print(H, M, S)