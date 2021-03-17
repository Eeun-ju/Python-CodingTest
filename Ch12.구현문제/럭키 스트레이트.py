#럭키 스트레이트

n = str(input()) #input 크기 99,999,999 너무 크다 -> input으로 받을 수 있는
leftsum = 0
rightsum = 0

for i in range(len(n)//2):
    leftsum += int(n[i])
    rightsum += int(n[i+len(n)//2])

if leftsum==rightsum :
    print('LUCKY')
else:
    print('READY')
                
