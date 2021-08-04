n = int(input())

for i in range(n):
    cnt, word = input().split()
    for j in word:
        print(j*int(cnt), end='')
    print()