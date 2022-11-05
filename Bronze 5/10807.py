n = int(input())
list = list(map(int,input().split()))
v = int(input())
cnt = 0

for i in list:
    if i == v:
        cnt += 1
    else:
        continue
print(cnt)

# print(list.count(v))