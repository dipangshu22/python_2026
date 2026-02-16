from functools import reduce

l=[33,23,43,56,78,56]

data=reduce(lambda x,y:x*y,l)

print(data)