n=int(input())
for i in range(1,n+1):
  outLine=list(str(x)+'*'+str(i)+'={:<4}'.format(str(x*i)) for x in range(1,i+1))
  print(''.join(outLine))