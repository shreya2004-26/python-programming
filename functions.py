def my_func(a,b):
    c=a+b
    d=a-b
    return c,d

a,b = my_func(2,3)
print("The returned values are: ",a,"&",b)

x = lambda a,b,c :a+b-c
print("values returned are:",x(2,6,5))


