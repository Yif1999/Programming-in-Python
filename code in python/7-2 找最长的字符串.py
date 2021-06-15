N=int(input())
l=[]
for i in range(N):
  l.append(input())
res=max(l,key=len)
print('The longest is: {}'.format(res))