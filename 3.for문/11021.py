import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    # add = a+b
    print("Case #%d: %d" %(i+1,a+b))
