n = int(input())
a = input().split()

result = [1,1]
for i in range(len(a)):
    if a[i] == 'R':
        result[1] += 1
    elif a[i] == 'L':
        result[1] -= 1
    elif a[i] == 'U':
        result[0] -= 1
    else:
        result[0] +=1

    if result[0]<1:
        result[0] +=1
    elif result[0]>5:
        result[0] -= 1
    elif result[1]<1:
        result[1] +=1
    elif result[1]>5:
        result[1] -= 1
print(result)
    
    
'''
n = int(input())
a = input().split()

x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
types = ['L','R','U','D']

for plan in a:
    for i in range(len(types)):
         if plan == types[i]:
             nx = x+dx[i]
             ny = y + dy[i]
    if nx <1 or ny>n or nx>n or ny<1:
        continue
    x,y = nx, ny
'''
