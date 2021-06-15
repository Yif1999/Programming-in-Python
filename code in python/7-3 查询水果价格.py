print('[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit')
cmd=list(map(int,input().split()))
for i in range(5):
  if cmd[i]==0 :
    break
  elif cmd[i]==1:
    print('price = 3.00')
  elif cmd[i]==2:
    print('price = 2.50')
  elif cmd[i]==3:
    print('price = 4.10')
  elif cmd[i]==4:
    print('price = 10.20')
  else:
    print('price = 0.00')
