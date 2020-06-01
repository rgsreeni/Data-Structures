# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:31:17 2020

@author: rgsre
"""

class node:
    def __init__(self,value):
        self.value = value
        self.front = None
        self.rear = None
class queue:
    def __init__(self):
        self.head = None
    def enq(self,value):
        if not self.head:
            self.head = node(value)
        else:
            self.head.rear = node(value)
            self.head.rear.front = self.head
            self.head = self.head.rear
    def deq(self):
        if self.head:
            while self.head.front:
                self.head = self.head.front
            if self.head.front == None and self.head.rear != None:
                self.head = self.head.rear
                self.head.front = None
            elif self.head.front == None and self.head.rear == None:
                self.head = None
    def printq(self):
        if self.head:
            temp = self.head
            while self.head.front:
                if self.head.rear == None:
                    print("joinQ",end = '-')
                print(self.head.value,end = '-' )
                self.head = self.head.front
            print(self.head.value,end = '-' )
            self.head = temp
        else:
            print("No elements in the Queue")
    def peek(self):
        if self.head and self.head.front != None:
            return self.head.front.value
        elif self.head and self.head.front == None:
            return self.head.value
        else:
            print("Empty Queue")
            

b = queue()

b.enq(6)

b.enq(5)

b.enq(4)    