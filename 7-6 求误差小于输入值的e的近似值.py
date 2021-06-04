import math
error=eval(input())
e_i=1
e_j=2
n=2
while e_j-e_i>=error:
  e_i=e_j
  e_j+=1/(math.factorial(n))
  n+=1
print('{:.6f}'.format(e_j))