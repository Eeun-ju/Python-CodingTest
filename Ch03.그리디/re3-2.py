#큰 수의 법칙

def solution(n,m,k,data):
    answer = 0

    data.sort()
    se_data = data[-2]

    while 1:
        for _ in range(k):
            if m == 0:
                break
            answer += data[-1]
            m -=1
            

        if m == 0:
            break
        answer += se_data
        m-=1
        
    
    return answer
