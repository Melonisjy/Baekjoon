n = int(input())
car_list = list(map(int,input().split()))
count = 0

for i in car_list:
    if i == n:
        count += 1

print(count)