n = int(input())

for i in range(n):
    scores = list(map(int,input().split()))
    avg = sum(scores[1:])/scores[0]

    count = 0

    for j in scores[1:]:
        if j > avg:
            count += 1

    per = (count/scores[0]) * 100
    print('%.3f' %per + '%')
