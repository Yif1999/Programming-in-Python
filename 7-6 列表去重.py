old_lst=eval(input())
new_lst=[]
for i in old_lst:
  if i not in new_lst:
    new_lst.append(i)
print(*new_lst,sep=' ')