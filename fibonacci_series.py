inp=int(input("enter upto what length u want to print:"))
a=0
b=1
c=0
print(a)
print(b)
for i in range(2,int(inp)):
        c=a+b
        print(c)
        a=b
        b=c
