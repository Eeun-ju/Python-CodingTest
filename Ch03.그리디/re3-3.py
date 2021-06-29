#숫자 카드 게임

def solution(n,m,data):
    answer = 0
    mini_row = []
    for i in range(n):
        mini_row.append(min(data[i]))

    answer = max(mini_row)
    return answer
