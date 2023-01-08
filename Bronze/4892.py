num = 0

while True:
    n_0 = int(input())
    num += 1
    if n_0 == 0:
        break
    else:
        n_1 = 3 * n_0
        if n_1 % 2 == 0:
            s = 'even'
            n_2 = n_1/2
        else:
            s = 'odd'
            n_2 = (n_1+1) / 2
        n_3 = 3 * n_2
        n_4 = n_3 // 9
        print(num,'.',sep='',end='')
        print( '',s, "%d" %(n_4))
