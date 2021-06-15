n=int(input())
for i in range(1,n//2+2):
  print('{:^11}'.format('*'*(2*i-1)))
for i in range(n//2,0,-1):
  print('{:^11}'.format('*'*(2*i-1)))