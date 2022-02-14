a = int(input())
b = int(input())
c = int(input())

arr = [a, b, c]
arr.sort()

if arr[0] == arr[1] == arr[2] == 60:
    print("Equilateral")
elif arr[0] + arr[1] + arr[2] == 180 and arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
    print("Isosceles")
elif arr[0] + arr[1] + arr[2] == 180 and arr[0] != arr[1] != arr[2]:
    print("Scalene")
elif arr[0] + arr[1] + arr[2] != 180:
    print("Error")

