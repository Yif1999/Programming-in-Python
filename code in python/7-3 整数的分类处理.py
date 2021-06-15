n=int(input())
lst=list(map(int,input().split()))

max=0
for i in lst:
  if i%3==0 and i>max:
    max=i
if max==0:
  print('NONE',end=' ')
else:
  print(max,end=' ')

count=0
for i in lst:
  if (i-1)%3==0:
    count+=1
if count==0:
  print('NONE',end=' ')
else:
  print(count,end=' ')

num=[]
for i in lst:
  if (i-2)%3==0:
    num.append(i)
if num==[]:
  print('NONE',end='')
else:
  print("{:.1f}".format(sum(num)/len(num)))