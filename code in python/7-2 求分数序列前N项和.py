N=int(input())
Sum=0 
numerator=2
dinominator=1
for i in range(N):
  Sum+=numerator/dinominator
  temp=numerator+dinominator
  dinominator=numerator
  numerator=temp
print('{:.2f}'.format(Sum))