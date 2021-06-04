n=input()
count=0
if '3' in n or '6' in n or '9' in n:
  print('淘淘不会数'+n)
else:
  N=int(n)
  for i in range(1,N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
      continue
    count+=i
  print(count)  