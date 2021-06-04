s1=input()
s2=[]
for i in s1:
  if i.isupper() and i not in s2:
    s2.append(i)
if len(s2)<1:
  print('Not Found')
else:
  print(''.join(s2))
