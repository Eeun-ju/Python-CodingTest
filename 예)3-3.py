n,m = map(int,input().split())

result = 0
for i in range(n):
    data = list(map(int,input().split()))

    mini = min(data)

    result = max(mini,result)

print(result)
