n = int(input())

data = []
for i in range(n):
    k = int(input())
    data.append(k)
data = sorted(data,reverse=True)

for i in data:
    print(i,end = ' ')
    
