# -*- coding: utf-8 -*-
def count_13(x):
    count1=0
    count3=0
    n=[int(y) for y in str(x)]
    for i in n:
        if i==1:
            count1+=1
        elif i==3:
            count3+=1
    (a,b)=(count1,count3)    
    return (a,b)
x=int(input('enter integer'))
print(count_13(x))
