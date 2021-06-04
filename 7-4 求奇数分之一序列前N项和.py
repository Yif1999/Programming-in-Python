import math

n=int(input())
N=list(range(1,n))
S=1
for i in N:
  S=S+1/(1+2*i)
print("sum={0:.6f}".format(S))
