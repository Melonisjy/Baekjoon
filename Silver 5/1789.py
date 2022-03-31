S = int(input())

temp = 1
count = 0

while True:
    S -= temp
    if S >= 0:
        temp += 1
        count += 1
    else:
        print(count)
        break