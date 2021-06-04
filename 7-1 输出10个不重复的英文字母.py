s1=input()
s2=[]
for i in s1:
  if i.isalpha() and i.upper() not in s2 and i.lower() not in s2:
    s2.append(i)
  if len(s2)==10:
    break
if len(s2)<10:
  print('not found')
else:
  print(''.join(s2))
