import sys

T = int(input()) # test case

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
