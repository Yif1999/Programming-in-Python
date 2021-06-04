str=input()
str16= "0123456789ABCDEFabcdef"
new_str=''
count=0
index=0
for i in str:
  if i in str16:
    new_str=new_str+i
    if index!=0 and str[index-1]=='-':
      count+=1
  index+=1
if len(new_str)>0:
  num=int(new_str,16)*(-1)**count
  print(num)
