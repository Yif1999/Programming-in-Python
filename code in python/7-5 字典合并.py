dic1=eval(input())
dic2=eval(input())
for i in dic2:
  if i in dic1:
    dic1[i]+=dic2[i]
  else:
    dic1[i]=dic2[i]
res=sorted(dic1.items(),key=lambda x:ord(x[0]) if type(x[0])==str else x[0])
print((str(dict(res)).replace("'",'"')).replace(' ',''))