#만들 수 없는 금액

import itertools

n = int(input())
data = list(map(int,input().split()))

result = []
for i in range(1,n+1):
    combi = list(itertools.combinations(data,i))

    for j in range(len(combi)):
        result.append(sum(combi[j]))
num = 1
while 1:
    if num not in result:
        print(num)
        break
    num += 1

'''
data.sort()
target = 1
for x in data:
    if target <x:
        break
    target+=x

print(target)
'''
