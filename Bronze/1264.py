arr = ['a', 'e', 'i', 'o', 'u']

while True:
    count = 0

    s = list(input().lower())
    if s[0] == '#':
        break
    for i in s:
        if i in arr:
            count += 1

    print(count)