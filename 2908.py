a, b = map(list,map(str,input().split()))
a.reverse()
b.reverse()

a_reverse = "".join(a)
b_reverse = "".join(b)

if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)