while True:
    n = int(input())
    measure = []
    if n != -1:
        for i in range(1, n):
            if n % i == 0:
                measure.append(i)
            else:
                continue
        if sum(measure) == n:
            print(n, "= ", end="")
            print(*measure, sep=" + ")
        else:
            print('%d is NOT perfect.' %n)
    else:
        break

