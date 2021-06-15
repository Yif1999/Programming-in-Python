def prime(p):
  if p==1:
    return False
  isSuShu=1
  for i in range (2,p):
    if p%i==0:
      isSuShu=0
  if isSuShu:
    return True
  else:
    return False

def PrimeSum(m,n):
  Sum=0
  for i in range(m,n+1):
    if prime(i):
      # print(str(i)+'is prime\n')
      Sum+=i
  return Sum

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))