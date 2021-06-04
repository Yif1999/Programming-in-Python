N=int(input())
i,j=1,1
n=0
while n<N:
  n=i+j
  i,j=j,n
print(n)