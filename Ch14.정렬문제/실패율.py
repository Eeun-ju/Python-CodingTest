#실패율

def solution(N, stages): # 스테이지 개수, 게임을 이용하는 사용자가 멈춰있는 스테이지 번호 배열
    answer = []
    length = len(stages)
    # 실패율 = 스테이지 도달 but 클리어x / 스테이지 도달 플레이어 수
    
    for i in range(1,N+1):
        clear = stages.count(i)
        
        if length == 0:
            fail = 0
        else : 
            fail = clear/length
        
        answer.append((i,fail))
        length -= clear
    
    answer = sorted(answer, key = lambda t: t[1], reverse= True)
    answer = [i[0] for i in answer]
    #실패율이 높은 스테이지부터 내림차순으로 return
    return answer
