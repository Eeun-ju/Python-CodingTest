#상하좌우

def solution(n,data):
    x,y = 1,1
    #U,D,L,R
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move = ['L','R','U','D']
    for plan in data:

        for i in range(4):
            if plan == move[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny<1 or nx>n or ny >n:
            continue

        x,y = nx,ny

    return x,y
        
            
        
