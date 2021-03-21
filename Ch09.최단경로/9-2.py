import deapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dis,now = heapq.heappop(q)

        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist i[1]

            if cost <
