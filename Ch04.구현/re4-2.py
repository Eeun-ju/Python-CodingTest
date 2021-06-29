# 시간에서 숫자 세기

def solution(h):

    answer = 0

    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    answer += 1
    return answer
