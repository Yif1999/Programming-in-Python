lst1=input().split()
lst2=input().split()
rst=[]
for i in lst1:
  if i not in lst2:
    rst.append(i)
for j in lst2:
  if j not in lst1 and j not in rst:
    rst.append(j)
for k in rst:
  if rst.index(k)==0:
    print(k,end='')
  else:
    print(" "+k,end='')
  