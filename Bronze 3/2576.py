lst = []
even = [] # 짝수
odd = [] # 홀수
cnt = 0

for i in range(7):
    lst.append(int(input()))

for i in range(len(lst)):
    if lst[i] % 2 == 0: # 짝수이면
        even.append(lst[i])
        cnt += 1
    else:
        odd.append(lst[i])


if cnt == 7:
    print('-1')
else:
    print(sum(odd))
    print(min(odd))

