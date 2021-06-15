N=int(input())
if N:
  score=list(map(int,input().split()))
  print('average = {:.1f}'.format(sum(score)/N))
  print('count =',sum(i>=60 for i in score))
else:
  print('average = 0.0\ncount = 0')