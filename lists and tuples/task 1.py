# -*- coding: utf-8 -*-
def add_lists(a,b):
    c=[]
    for i in range(len(a)):
        x=a[i]+b[i]
        c.append(x)
    return c
a=[]
b=[]
x=int(input('enter length of lists'))
for i in range (x):
    y=int(input('enter element for list a'))
    a.append(y)
    z=int(input('enter element for list b'))
    b.append(z)
    
new_list=add_lists(a, b)
print (new_list)
