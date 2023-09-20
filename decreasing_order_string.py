inp=input("please enter a string:")
characterform=list(inp)
print(characterform)
print(len(characterform))
x=(len(characterform))
for i in range (ord('a'),ord('z')+1):
    m=0
    for k in range(0,int(x)):
        if(chr(i)==characterform[k]):
            m+=1
    if(m>0):
        print(chr(i),m)