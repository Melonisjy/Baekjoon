s, k, h = map(int,input().split())
arr = [s, k, h]
arr.sort()

if s+k+h >= 100:
    print('OK')
else:
    if arr[0] == s:
        print('Soongsil')
    elif arr[0] == k:
        print('Korea')
    else:
        print('Hanyang')