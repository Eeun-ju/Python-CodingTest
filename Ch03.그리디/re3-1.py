#거슬러 주어야 할 동전의 최소 개수

def solution(n): # n원
    answer = 0

    coin = [500,100,50,10]

    for c in coin:
        m = n//c

        answer += m
        n = n - c*m
        
    return answer
