cute, no_cute = 0, 0
for i in range(int(input())):
    n = int(input())
    if n == 1:
        cute += 1
    elif n == 0:
        no_cute += 1

if cute > no_cute:
    print("Junhee is cute!")
elif cute < no_cute:
    print("Junhee is not cute!")