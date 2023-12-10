# -*- coding: utf-8 -*-
def common_elements(list1,list2):
    common_elements=[]
    
    for i in list1:
        if i in list2:
               common_elements.append(i)
         
    return common_elements        
list1=[1,2,3,3,4,4,5]
list2=[2,2,3,3,4,5]
print (common_elements(list1, list2))