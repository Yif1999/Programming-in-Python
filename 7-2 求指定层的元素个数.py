def layer_count(items,n,layer,s):
  for i in items:
    if isinstance(i,list):
      s=layer_count(i,n+1,layer,s)
    else:
      if n==layer:
       s+=1
      elif n>layer:
        return s
  else:
    return s

items=eval(input())
layer=int(input())
print(layer_count(items,1,layer,0))