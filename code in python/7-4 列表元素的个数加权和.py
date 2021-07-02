lst=eval(input())

def Sum(lst,level,s):
    for i in lst:
        if type(i)==list:
            s+=Sum(i,level+1,0)
        else:
            s+=10-level
    return s

print(Sum(lst,0,0))
