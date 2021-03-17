#곱하기 혹은 더하기

S = input()
result = 0

if int(S[0])+int(S[1]) <= int(S[0])*int(S[1]):
    result = result + int(S[0])*int(S[1])
else:
    result = result + int(S[0])+int(S[1])
    
for i in range(2,len(S)):
    if result*int(S[i]) <= result + int(S[i]):
        result = result + int(S[i])
    else:
        result = result*int(S[i])

print(result)
