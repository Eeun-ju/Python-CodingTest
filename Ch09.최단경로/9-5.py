#전보->플로워셜?

n,m,c = map(int,input().split()) #도시 수, 통로 수, 출발 도시(메시지 출발)
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for i in range(m):
    start,end,cost = map(int, input().split())
    graph[start][end] = cost

for a in range(1,n+1):
    for b in range(1,n+1):
        for k in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
total_city = 0
total_cost = 0
for i in graph[c]:
    if i<INF and i>0:
        total_cost = max(total_cost,i)
        total_city += 1
print(total_city,end=' ')
print(total_cost)
# 도시의 수와 걸리는 시간

