# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:33:33 2020

@author: rgsre
"""

class node:
    def __init__(self,value):
        self.value = value
        self.top = None
        self.bottom = None
        
class stack:
    def __init__(self):
        self.head = None
    
    def push(self,value):
        if not self.head:
            self.head = node(value)
        else:
            self.head.top = node(value)
            self.head.top.bottom= self.head
            self.head= self.head.top
    def printstack(self):
        if self.head:
            temp =self.head
            while self.head:
                print("^ \n",self.head.value)
                self.head = self.head.bottom
            self.head = temp
    def pop(self):
        if self.head:
            if self.head and self.head.bottom:
                self.head  = self.head.bottom
                self.head.top = None
            else:
                self.head = None
 

a = stack()

a.push(4)

a.push(5)

a.push(6)       