n,m = map(int,input().split())
x,y,b = map(int,input().split())

d = [[0]*m for _ in range(n)]
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

d[x][y] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

turn = 0
count = 1

def turn_left():
    global b
    b-=1
    if b == -1:
        b = 3
        
while 1:
    turn_left()

    nx = x + dx[b]
    ny = y + dy[b]

    if d[nx][ny]==0 and data[nx][ny] == 0:
        d[nx][ny]= 1
        x = nx
        y = ny
        count +=1
        turn = 0
    else:
        turn +=1

    if turn == 4:
        nx = x-dx[b]
        ny = y-dy[b]

        if d[nx][ny] == 0:
            x=nx
            y = ny
        else:
            break

        turn = 0
print(count)
        
    
