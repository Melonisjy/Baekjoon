A = int(input())
B = int(input())
C = int(input())

D = A*B*C
D_list = list(str(D))
for i in range(10):
    D_num_count = D_list.count(str(i))
    print(D_num_count)