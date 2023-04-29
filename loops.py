# a = [1,2,(2,3),"Neetu","hii",{1:200,2:300},{3,4}]
# for i in a:
#     print(i)

# for i in range(0,12,2):
#     print(i)

# a = [2,3,4,5,6,7]
# for i in a:
#     if i==4:
#         break;
#     print(i)
# ctrl + / to comment multiple lines at once
a = [2,4,2,1,5,6,7,0]
for i in a:
    if i == 5:
        break;
    print(i)

a = [2,4,2,1,5,6,7,0]
for i in a:
    if i == 5:
        continue;
    print(i)

print("/")
a=1
while a<5:
    print(a)
    a=a+1
