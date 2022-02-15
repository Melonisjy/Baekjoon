a = int(input()) # x사의 1리터당 요금
b = int(input()) # y사의 기본요금
c = int(input()) # y사의 요금이 기본요금이 되는 사용량의 상한금
d = int(input()) # y사의 1리터당 추가 요금
p = int(input()) # 한달 간 수도의 사용량

X = a * p # x사의 한달 수도 요금
Y = 0 # y사의 한달 수도 요금

if p < c:
    Y += b

elif p > c:
    Y += b + (p - c) * d

print(min(X, Y))

