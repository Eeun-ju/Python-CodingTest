n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
se_data = data[-2]
result = 0

while 1:
    for i in range(k):
        result = result + max(data)
        m = m-1
        if m == 0:
            break
    result += se_data
    m -=1
    if m == 0:
        break
print(result)
            
