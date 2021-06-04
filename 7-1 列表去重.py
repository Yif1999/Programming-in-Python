lst=eval(input())
lst_derpt=list(set(lst))
lst_derpt.sort(key = lst.index)
print(' '.join(map(str,lst_derpt)))