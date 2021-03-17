#모험가 길드

n = int(input())

data = list(map(int,input().split()))

# 우선 정렬하기
data.sort()
result = 0 #그룹 수
count = 0 #그룹 공포 지수

for i in data:
    count+=1

    if count >=i:
        result +=1
        count = 0
print(result)
