a, b, c = map(int,input().split())

first = a * b / c
second = a / b * c
print('%d' %(max(first, second)))