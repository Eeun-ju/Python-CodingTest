#전보->한 도시에서 다른 도시까지의 최단 거리 문제 => 다익스트라 알고리즘
import heapq
import sys      #입력이 매우 크다 -> sys와 queue사용

INF = int(1e9)
input = sys.stdin.readline

n,m,c = map(int,input().split()) #도시 수, 통로 수, 출발 도시(메시지 출발)


graph = [[]for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    start,end,cost = map(int, input().split())
    graph[start].append((end,cost))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입한다.
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
            
total_city = 0
total_cost = 0

for d in distance:
    if d!=INF:
        total_cost = max(total_cost,d)
        total_city += 1
print(total_city-1,end=' ')
print(total_cost)
# 도시의 수와 걸리는 시간
