# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:28:36 2022

@author: Marry
"""

class bank_account(object):
    def __init__(self,account_num,name,balance):
        self.account_num=account_num
        self.name=name
        self.balance=balance
    def deposit(self):
        deposit=int(input('enter amount to be deposited:'))
        self.balance+=deposit
        print ('current balance after deposit is:'+' '+ str(self.balance))
    def withdrawal(self):  
        withdraw=int(input('enter amount to withdraw:'))
        self.balance-=withdraw
        print ('current balance after withdraw is:'+' '+ str(self.balance))
    def bank_fees(self):
        return (self.balance*0.05)
        
    def display(self):
        print ('account name:',self.name)
        print ('account balance:',self.balance)
        print ('account number:',self.account_num)
a=bank_account(12345,'alice',30000)
a.display()
a.deposit()
a.withdrawal()
print (a.bank_fees())        