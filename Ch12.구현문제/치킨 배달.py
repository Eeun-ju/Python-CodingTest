#치킨 배달
import itertools

n,m = map(int,input().split())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))
mini = 99,999,999
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            home.append((i,j))
        elif data[i][j] == 2:
            
            chicken.append((i,j))

#m개 고르기 combination 필요
            
chicken_locate = list(itertools.combinations(chicken,m))
total = []
#m개 고른 쌍에서
for i in range(len(chicken_locate)):
    cost = 0    # m개 선택 치킨 거리 초기화
    for r,c in home: # 집 위치에서
        mini = 999,999
        distance = [] # 집과 치킨집 거리 최소 찾기 위한 list
        
        for j in range(0,m):
            위치 = chicken_locate[i][j]
            distance.append((abs(r-위치[0]) + abs(c-위치[1]))) #계산 거리 모두 넣기
        cost += min(distance) # 거리 중 가장 최소 거리 찾아 
    total.append(cost)
print(min(total))
