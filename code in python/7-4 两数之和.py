lst=list(map(int,input().split(',')))
n=int(input())
diff={}
flag=1
for i in lst:
  diff[i]=n-i
for j in diff:
  if diff[j] in lst:
    flag=0
    print(lst.index(j),lst.index(diff[j]))
    break
if flag:
  print('no answer')