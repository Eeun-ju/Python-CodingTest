def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#노드 개수와 간선의 개수 입력
v,e = map(int,input().split())
parent = [0]*(v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i
#union 연산
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print('원소가 속한 집합 : ',end = '')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블: ',end = '')
for i in range(1,v+1):
    print(parent[i],end=' ')
