#1일 될 때까지

def solution(n,k):
    answer = 0

    while 1:
        if n == 1:
            break
        
        
        if n%k == 0:
            n = n/k
            
        else:
            n -= 1
        answer +=1
    return answer
