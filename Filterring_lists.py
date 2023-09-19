lists=[]
lists2=[]
inp=input("enter the size in list:")
for i in range(0,int(inp)):
    element=input()
    lists.append(element)
    if int(element) > 0 :
        lists2.append(element)
    
print(lists)
print('filtered list is :')
print(lists2)

    
    

