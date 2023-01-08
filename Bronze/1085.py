x, y, w, h = map(int,input().split())

x1 = w-x
y1 = h-y

print(min(x, x1, y, y1))