x= lambda a: 10/a
print(x(2))

x= lambda a,b,c: a*b*c
print(x(2,3,4))

def myfunc(n):
    return lambda a:a*n
myDoubler=myfunc(2)
print(myDoubler(11))


