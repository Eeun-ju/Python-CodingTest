#서로소 집합을 활용한 사이클 판별
#무방향 그래프 사이클 판별하기

def find_parent(parent,x):
    #루트 노드가 아니라면 루트 노드 계속 찾아주기
    if parent[x]!=x:
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
parent = [0]*(v+1) #부모 테이블

for i in range(1,v+1):
    parent[i] = i
    #자기 자신으로 초기화
cycle = False

for i in range(e):
    a,b = map(int,input().split())
    #사이클 수보다 사이클의 여부를 확인 하므로 최소의 연산을 위해서는 발견 즉시 멈춘다.    
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
