a, b = map(int,input().split())

max_n = max(a, b)
min_n = min(a, b)
d = max_n - min_n

sum = (d * (d+1))//2
print(sum + min_n * (d+1))