n=int(input())
if n<4:
  print('1')
elif n==4:
  print('1\n4150\n4151')
else:
  print('1\n4150\n4151')
  # extend=''
  extend=[]
  for i in range(10000,10**n):
    s=str(i)
    Sum=sum([int(j)**5 for j in s])
    if Sum==i:
      # extend+=(s+'\n')
      extend.append(i)
  for k in extend:
    print(k)