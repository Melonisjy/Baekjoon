array = []
for i in range(10):
    n = int(input())
    array.append(n % 42)

array = set(array)
print(len(array))
print(array)