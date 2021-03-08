n,k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B,reverse = True)
for i in range(k):
    A[i],B[i] = B[i],A[i]

print(sum(A))
