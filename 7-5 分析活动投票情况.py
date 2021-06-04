count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
statistic=list(map(int,input().split(',')))
for i in statistic:
  count[i]+=1
lst=[]
for j in range(6,11):
  if count[j]==0:
    lst.append(str(j))
print(' '.join(lst))