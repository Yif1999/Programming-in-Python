from math import sqrt
j,k=input().split()
j,k=int(j),int(k)
noWanShu=1
for i in range(j,k+1):
  num=[]
  for n in range(2,int(sqrt(i)+1)):
    if i%n==0:
      num.append(n)
      num.append(i//n)
  num.append(1)
  if sum(num)==i:
    num.sort()
    print(str(i),'=',' + '.join(list(map(str,num))))
    noWanShu=0
if noWanShu:
  print(None)