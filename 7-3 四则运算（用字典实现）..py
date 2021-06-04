x=int(input())
operator=input()
y=int(input())
compute={'+':'x+y','-':'x-y','*':'x*y','/':'x/y'}
try:
  result=eval(compute[operator])
  print("{:.2f}".format(result))
except:
  print("divided by zero")