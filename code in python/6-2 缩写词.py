def acronym(s):
  s_list=s.split()
  short=''
  for i in s_list:
    short+=i[0].upper()
  return short


phrase=input()
print(acronym(phrase))