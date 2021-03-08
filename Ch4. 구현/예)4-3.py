location = input()

first = location[0]
locate = [0,0]
result = 8
if first == 'a':
    locate[0] = 1
elif first == 'b':
    locate[0] = 2
elif first == 'c':
    locate[0] = 3
elif first == 'd':
    locate[0] = 4
elif first == 'e':
    locate[0] = 5
elif first == 'f':
    locate[0] = 6
elif first =='g':
    locate[0] = 7
else:
    locate[0] = 8

locate[1] = int(location[1])

h = [-2,2]
v = [-1,1]
for i in range(2):
    x,y = locate
    if i==0:
        for j in h:
            for k in v:
                x,y = locate
                x = x + j
                y = y + k
                if x<1 or x>8 or y<1 or y>8:
                    result-=1
    else:
        for j in h:
            for k in v:
                x,y = locate
                x = x + k
                y = y + j
                if x<1 or x>8 or y<1 or y>8:
                    result-=1
print(result)

total = 0
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,2),(1,-2)]
for step in steps:
    next_row = locate[1] + step[0]
    next_col = locate[0] + step[1]

    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
        total +=1    
    
        
print(total)
