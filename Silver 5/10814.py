import sys
n = int(sys.stdin.readline())

inf = []

for i in range(n):
    a, b = map(str,sys.stdin.readline().split())
    inf.append([int(a), i, b])

inf.sort()
for i in range(len(inf)):
    print("%d %s" %(inf[i][0], inf[i][2]))