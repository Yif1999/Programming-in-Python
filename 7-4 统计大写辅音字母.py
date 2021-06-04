str=input()
yy=['A','E','I','O','U']
count=0
for i in str:
  if 'A'<=i<='Z' and i not in yy:
    count+=1
print(count)