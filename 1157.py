alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = str(input()).upper()
char_maxnum = 0

for char in alphabet:
    char_num = word.count(char)
    if char_num > char_maxnum:
        char_maxnum = char_num

max_alphabets = []
for char in alphabet:
    if word.count(char) == char_maxnum:
        if max_alphabets:
            max_alphabets.append(char)
            print("?")
            break
        else:
            max_alphabets.append(char)

if len(max_alphabets) == 1:
    print(max_alphabets[0])
