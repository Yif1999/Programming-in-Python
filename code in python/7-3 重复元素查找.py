true=0
false=0

row=int(input())
for i in range(row):
  items=input().split()
  item_set=set(items)
  if len(items)>len(item_set):
    true+=1
  else:
    false+=1
print("True=",true)
print("False=",false)