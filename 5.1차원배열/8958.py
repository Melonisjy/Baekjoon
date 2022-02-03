n = int(input())

for i in range(n):
    cnt = 0
    grade = 0
    answer = list(str(input()))
    for j in answer:
        if j == 'O':
            cnt += 1
            grade += cnt
        else:
            cnt = 0

    print(grade)

