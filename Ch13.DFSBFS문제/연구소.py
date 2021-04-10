#연구소

#3개 설치하는 모든 겨우의 수를 다 계산

n,m = map(int,input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

#바이러스 퍼지게 만들기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >=0 and nx <n and ny >=0 and ny <m:
            #바이러스 퍼질 수 있는 경우
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                # 그 위치에서 다시 재귀적 실행
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전 영역의 최댓값 계
        result = max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count+=1
                dfs(count)
                data[i][j] = 0
                count -=1

dfs(0)
print(result)
