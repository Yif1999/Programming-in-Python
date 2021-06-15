a,b=map(int,(input().split()))
add=0
count=1
for i in range(a,b+1):
  print('{:>5}'.format(i),end=('\n' if count%5==0 else ''))
  add+=i
  count+=1
else:
  print(('' if (count-1)%5==0 else '\n')+'Sum =',add)