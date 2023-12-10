# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:29:19 2022

@author: Marry
"""

class computation(object):
    def __init__(self):
        pass
    def factorial (self,n):
        factorial=1
        for i in range (1,n+1):
            factorial=factorial*i
        return factorial
    def Sum (self,n):
        sum=0
        for i in range (1,n+1):
            sum=sum + i
        return sum
    def test_prim(self,n):
        for i in range (2,n):
            if n%i==0:
                return False
        return True
    def test_prims(self,n,m):
        div=0
        for i in range (1,n+1):
            if n%i==0 and m%i == 0:
                div=div+1
        if div==1:
            return True
        else:
            return False
        
    def Table_mult(self,n):
        for i in range (1,11):
            print (i,'*',n,'=',(i*n))
    def all_tableMult(self,n):
        for i in range (1,n+1):
            print ('table of',i,'is:')
            for j in range (1,11):
                print (i,'*',j,'=',i*j)
    def listDiv(self,n):
        listdiv=[]
        for i in range (1,n+1):
            if n%i==0:
                listdiv.append(i)
        return listdiv
    def listDivPrime(self,n):
         L=[]
         for i in range (1,n+1):
             if n%i==0 and self.test_prim(i):
                 L.append(i)
         return L        
a=computation()
print (a.factorial(4))
print (a.Sum(4))
print (a.test_prim(4))
print (a.test_prims(4,5))
a.Table_mult(4)       
a.all_tableMult(4)      
print (a.listDiv(4))
print (a.listDivPrime(4))      
                
        