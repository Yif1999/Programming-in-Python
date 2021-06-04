n=int(input())
print("{0:.3f}".format(sum([float(i/(2*i-1)*(-1)**(i+1)) for i in range(1,n+1)])))