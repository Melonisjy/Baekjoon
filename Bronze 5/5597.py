students = [i for i in range(1,31)]

for i in range(28):
    data = int(input())
    students.remove(data)
print(min(students))
print(max(students))