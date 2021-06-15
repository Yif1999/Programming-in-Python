n=int(input())
days_1=[31,28,31,30,31,30,31,31,30,31,30,31]
days_2=[31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(n):
  days=0
  date=list(map(int,input().split()))
  if date[0]<0 or date[1]>12 or date[1]<0 or date[2]<0 or date[2]>31:
    print('ErrorInput')
  else:
    isRunNian=0
    if (date[0]%4==0 and date[0]%100!=0) or date[0]%400==0:
      isRunNian=1
    if isRunNian:
      days=sum(days_2[:date[1]-1])+date[2]
    else:
      days=sum(days_1[:date[1]-1])+date[2]
    print('Totaldays=',days)