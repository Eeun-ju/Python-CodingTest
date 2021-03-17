#특정 거리의 도시 찾기

n,m,k,x = map(int,input().split())  # n개 노드, m개 도록, 거리 정보 k, 출발도시

INF = int(1e9)
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))

def get_smallest_node():

    min_value = INF
    index = 0

    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):

    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for j in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
    

dijkstra(x)
도시 = []
count = 0
for i in range(len(distance)):
    if distance[i]==k:
        도시.append(i)
    else:
        count += 1

if count == len(distance):
    print(-1)
else:
    도시.sort()
    for i in 도시:
        print(i)
    
