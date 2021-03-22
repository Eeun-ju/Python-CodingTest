#미래 도시

INF = int(1e9)

n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for i in range(m):
    start,end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1

x,k = map(int,input().split())

for a in range(1,n+1):
    for b in range(1,n+1):
        for k in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            #플로이드 워셜 알고리즘 사용
#1에서 k까지, k에서 x까지 이미 mini 값으로 들어가 있으므로 찾기만 하면 ok            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
    
