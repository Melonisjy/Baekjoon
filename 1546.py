n = int(input())
score_list = list(map(int,input().split()))
max_score = max(score_list)
result = 0

for i in range(0,n):
    score_list[i] = score_list[i]/max_score*100
    result = result + score_list[i]

result = result/n
print(result)