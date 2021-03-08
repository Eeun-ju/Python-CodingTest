n = int(input())

array = []
for i in range(n):
    a = input().split()

    array.append((a[0],int(a[1])))

array = sorted(array, key = lambda k: k[1])

for k in array:
    print(k[0], end=' ')
