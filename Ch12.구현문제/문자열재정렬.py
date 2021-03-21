#문자열 재정렬

s = str(input())
num = 0
alph = []
for i in s:
    #print(ord(i))
    if ord(i)>=49 and ord(i)<=57:   #아스키 코드 ord 사용하기 
        num += int(i)
    else:
        alph.append(i)
alph.sort()
for i in range(len(alph)):
    print(alph[i],end='')
    if i == (len(alph)-1):
        print(num)
#print(alph,str(num))
