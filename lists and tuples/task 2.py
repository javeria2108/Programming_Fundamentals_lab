# -*- coding: utf-8 -*-
def list_square(a):
    b=[]
    for i in a:
        x=i**2
        b.append(x)
    return b    
a=[]
x=int(input('enter list length')) 
for i in range(x):
    y=int(input('enter list elemnt'))
    a.append(y)
new_list=list_square(a)
print (new_list)    

