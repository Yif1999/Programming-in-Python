def CountDigit(number,digit):
  count=0
  for i in str(number):
    if i==str(digit):
      count+=1
  return count

number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)