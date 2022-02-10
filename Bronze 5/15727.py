L = int(input())
count = 0

count += L//5
if L % 5 != 0:
    count += 1


print(count)