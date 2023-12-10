# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:23:38 2022

@author: Marry
"""

class rectangle(object):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        return (2*(self.length+self.width))
    def area(self):
        return (self.width*self.length)
    def display(self):
        print ('length of rectangle is' +' '+ str (self.length))
        print ('width of ractangle is'+' '+ str(self.width))
        print ('area of rectangle is'+' ' +str(self.area()))
        print ('perimeter of rectangle is'+ ' ' +str(self.perimeter()))
a=rectangle(4,3)
a.display()        