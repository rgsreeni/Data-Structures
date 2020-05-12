# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:06:45 2020

@author: rgsrei
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
class Stack:
    def __init__(self):
        self.top = None
        self.size =  0
        
    def push(self,data):
        if self.top == None:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
        
    def printstack(self):
            if self.top == None:
                return None
            else:
                while self.top.next != None:
                    print(self.top.next.data, end = '->')
                    self.top = self.top.next
                print(self.top.next.data, end = '->')    
    def peek(self):
        return self.top.data
    
    def popp(self):
        print("popping",self.items[-1])
        self.items = self.items[:-1]