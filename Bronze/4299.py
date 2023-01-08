p, m = map(int,input().split())
if m > p or ((p+m)%2):
    print(-1)
else:
    p, m = (p+m)//2, (p-m)//2
    print(max(p, m),min(p, m))
