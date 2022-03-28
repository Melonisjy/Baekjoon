t = int(input())

for i in range(t):
    n = list(map(str, input().split()))
    answer = 0
    for j in range(len(n)):
        if j == 0:
            answer += float(n[j])
        else:
            if n[j] == "#":
                answer -= 7
            elif n[j] == "%":
                answer += 5
            elif n[j] == "@":
                answer *= 3

    print("%0.2f" % answer)