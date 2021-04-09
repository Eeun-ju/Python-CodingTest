#안테나

n = int(input())
data = list(map(int,input().split()))

length = max(data)+1
mini = 9999999999
result = -1
#처음부터 끝까지 찾지 말고 중간값에 해당하는 위치가 최소임을 생각하자.
'''
for i in range(1,length):
    distance = 0
    for j in data:

        distance += abs(j-i)

    if mini > distance:
        mini = distance
        result = i
    
'''
data.sort()
result = data[(n-1)//2]
print(result)
