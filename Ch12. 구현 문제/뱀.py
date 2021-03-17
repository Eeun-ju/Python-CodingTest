# 뱀
from collections import deque

n = int(input())    # 보드 크기
k = int(input())    # 사과 수

data = [[0]*n for i in range(n)]
for i in range(k):
    행,열 = map(int,input().split())
    data[행-1][열-1] +=1


    
l = int(input())
for li in range(n):
        print(data[li])
move = []
for i in range(l):
    move.append(list(input().split()))
# 현재 위치
현재 = [0,0]
data[현재[0]][현재[1]] = 2
times = 0
i = 0
방향x = [0,1,0,-1]
방향y = [1,0,-1,0]
방향 = 0
몸길이 = 1

queue = deque()
queue.append(현재)
while 1:
    
    print(현재)
    if int(move[i][0]) == times:
        #방향 바꾸기
        if move[i][1] == 'D':
            방향 += 1
        elif move[i][1] == 'L':
            방향 += -1
        i = i+1
    
    
    현재[0] += 방향x[방향]
    현재[1] += 방향y[방향]
    
    if (현재[0]<0 or 현재[0]>=n) or (현재[1]<0 or 현재[1]>=n):
        print(times+1)
        break
    
    if data[현재[0]][현재[1]] == 2:
        print(times+1)
        break
    
    if data[현재[0]][현재[1]] == 1:
        몸길이 += 1
        data[현재[0]][현재[1]] = 2
        
    elif data[현재[0]][현재[1]] == 0:
        제거 = queue.popleft()
        data[제거[0]][제거[1]] = 0
        # data[현재[0]-방향x[방향]*몸길이][현재[1]-방향y[방향]*몸길이] = 0
        data[현재[0]][현재[1]] = 2
    
    times += 1
    
