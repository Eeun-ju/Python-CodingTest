#볼링공 고르기

n,m = map(int,input().split())
data = list(map(int,input().split()))

result = 0

for i in list(set(data)):
    count = 0
    for j in data:
        if i == j:
            count += 1

    if count != 1:
        result += count*(count-1)//2
print(n*(n-1)//2 - result)
