def sum_with_weight(items,n,s):
  for i in items:
    if isinstance(i,list):
      s=sum_with_weight(i,n+1,s)
    else:
      s+=n*i
  else:
    return s


items=eval(input())
res=sum_with_weight(items,1,0)
print(res)