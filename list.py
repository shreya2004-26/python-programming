def my_func(a,b):
    c=a+b
    d=a-b
    return [c,d]

a = [1,3.0,"Bhopal","Shreya",[1,2,3],my_func(2,3)]
n = -1
print("element ",n," of the list is: ", a[n])
    
b = a[1:3] #here it will leave the element at last index
print("The sliced array is: ",b)

a[2] = "i changed you"
print("THe new list is: ", a)

a[0:3] = [100,200]
print(a)

e = a[3][2]
print(e)

a = [1,3.0,"Bhopal","Shreya",[1,2,3],my_func(2,3)]
print(a)
a.append("Ashya")
print(a)

index = 3
a[index] = "kuchh bhi"
print(a)

a=[1,2,3,4]
b=[4,5,6]
a.extend(b)
print(a)

r=a.index(5) #here it will return the index where 5 is present
print(r)

a.remove(5)
print(a)

a.sort(reverse=0)
print(a)

a.sort(reverse=1)
print(a)

a=["Hello",1,2,[1,2,3]]
print(a)
a.reverse()
print(a)
print(len(a))

a=[1,2,3]
b=[4,5,6,7]
print(a+b)