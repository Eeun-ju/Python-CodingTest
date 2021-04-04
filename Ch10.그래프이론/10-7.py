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


#서로소 집합 알고리즘 문
n,m = map(int,input().split())

parent = [0]*(n+1)

#부모 테이블 자기 자신으로
for i in range(0,n+1):
    parent[i] = i
for _ in range(m):
    oper,a,b = map(int,input().split())

    #합집합 경우
    if oper == 0:
        union_parent(parent,a,b)
    #찾기 경우
    elif oper == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')
    
    
    
