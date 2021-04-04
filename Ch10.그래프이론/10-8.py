#2개의 최소 신장 트리로 분할하기

def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0]*(v+1)

edges = [] #모든 간선을 담을 리스트와 최종 비용을 담을 변수
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b)) #비용과 간선 입력

edges.sort() #비용순으로 정렬
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b): #사이클 발생하지 않는 경우
        union_parent(parent,a,b)
        result += cost
        last = cost #가장 큰 비
print(result - last)
