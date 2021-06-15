n=int(input())
if n<5 or n>10:
  print("Error Input")
else:
  print(sum([int('8'*i) for i in range(1,n+1)]))