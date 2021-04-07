#국영수


n = int(input())
data = []
for _ in range(n):
    data.append(input().split())
    
# 국어, 영어, 수학, 이름 순으로 정렬

data.sort(key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for name in data:
    print(name[0])
'''

튜플을 원소로 하는 리스트 -> 각 튜플을 구성하는 원소의 순서에 맞게 정렬된다.
sort() 함수의  key 속성을 이용하여 정렬
-(int(x[1]) : 두번째 원소를 내림차순
int(x[2]) : 세번째 원소를 오름차순

'''
