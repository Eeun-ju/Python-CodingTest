#정수 엄청 크다 -> 이진탐색 생각해

def binary_search(array, target, start, end):
    while start<=end:

        mid = (start + end)//2

        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid -1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int,input().split()))

array.sort() # 반드시 이진 탐색 -> sort 필요

m = int(input())
target = list(map(int,input().split()))

for i in target:

    result = binary_search(array,i,0,n-1)

    if result != None:
        print('yes',end = ' ')
    else:
        print('no', end=' ')
