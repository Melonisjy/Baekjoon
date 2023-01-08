while True:
    angles = list(map(int,input().split()))
    angles.sort()
    if sum(angles) == 0:
        break
    if angles[2] ** 2 == angles[0] ** 2 + angles[1] ** 2:
        print("right")
    else:
        print("wrong")