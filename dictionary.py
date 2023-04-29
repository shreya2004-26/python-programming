# list/set can be only a key
# tuple can be both key/value

a = {1:2,(1,2):["College"],(1,2,3):"Classes",(2,3):{"Sucks"}}
print(a)
print("The element at this key is: ", a[(1,2,3)])

a = {1:100,2:200,3:300,4:400}
a[0] = 600
print(a)

a.pop(2)
print(a)

a[0]="python"
print(a)