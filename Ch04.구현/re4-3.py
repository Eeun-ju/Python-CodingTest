#왕실의 나이트

def solution(locate):
    if locate[0] == 'a':
        x = 1
    elif locate[0] == 'b':
        x = 2
    elif locate[0] == 'c':
        x = 3
    elif locate[0] == 'd':
        x = 4
    elif locate[0] == 'e':
        x = 5
    elif locate[0] == 'f':
        x = 6
    elif locate[0] == 'g':
        x = 7
    elif locate[0] == 'h':
        x = 8
    y = int(locate[1])
    
    answer = 0

    #L자 형태 이동
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [2,-2,1,-1,2,-2,1,-1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <1 or ny <1 or nx>8 or ny>8:
            continue
        answer +=1
        #print(nx,ny)
    return answer
