alphabet = "abcdefghijklmnopqrstuvwxyz"
word_list = []
word_num = []

S = str(input())

for i in S:
    word_list.append(i)

for character in alphabet:
    for i in range(len(word_list)):
        if character == word_list[i]:
            word_num.append(i)
            break
        elif i < len(word_list)-1:continue
        else:
            word_num.append(-1)
for i in word_num:
    print(i,end=" ")