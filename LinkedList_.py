# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:30:27 2020

@author: rgsre
"""

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkList:
    def __init__(self):
        self.head =  None 
        
    def addnode(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while self.head.next != None:
                self.head = self.head.next
            self.head.next = Node(value)
            self.head = temp
    
    def prepend(self,value):
        if self.head == None:
            self.head = Node(value) 
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node 
            
    def remove(self,value):
        if self.head != None:
            curr = prev = self.head 
            if curr.value == value:
                prev = curr.next
                curr.next = None
                self.head = curr = prev
            else:
                while curr.next != None:
                    prev = curr
                    curr = curr.next
                    if curr.value == value:
                        prev.next = curr.next
                        curr.next = None 
                prev = curr = self.head        
    
    def printlist(self):
       #initiate from self.head
       #print until sellf.head.next == None
       if self.head != None:
           if self.head.next == None:
               print(self.head.value)
           else:
               temp = self.head 
               while self.head.next != None:
                   print(self.head.value , end = '->')
                   self.head = self.head.next
               print(self.head.value , end = '->')
               self.head= temp        
    
    def rem_dup(self,value): 
        if self.head != None:
            curr = prev = self.head
            foc = False
            if curr.value == value:
                foc = True
            while curr != None and curr.next != None:
                prev = curr
                curr = curr.next
                
                if foc == True and curr.value == value:
                    prev.next = curr.next 
                    curr.next = None
                    curr = prev.next
                if curr != None and curr.value == value:
                    foc = True
            prev = curr = self.head
    
    def remall(self,value):
        curr = prev = self.head

        
        while curr.next != None:
            if curr.value != value:
                prev = curr
                curr = curr.next 
            elif curr.value == value and prev.value != value:
                prev.next = curr.next 
                curr.next = None
                curr = prev.next
            elif curr.value == value and prev.value == value:
                prev.next = curr.next
                prev = prev.next
                curr.next = None
                curr = prev
        if curr.value == value and curr.next == None:
            prev.next = None
            curr = None
            
            
            
#        
        curr = prev = self.head
        
    def deleteKey(self, key): 
        temp = self.head 
        prev = None
  
    # If head node itself holds the key  
    # or multiple occurrences of key 
        while (temp != None and temp.value == key): 
            self.head = temp.next # Changed head 
            temp = self.head         # Change Temp 
      
          # Delete occurrences other than head 
            while (temp != None): 
                # Search for the key to be deleted,  
                # keep track of the previous node  
                # as we need to change 'prev.next' 
                while (temp != None and temp.value != key): 
                    prev = temp 
                    temp = temp.next
          
        # If key was not present in linked list 
                if (temp == None): 
                    return self.head 
  
        # Unlink the node from linked list 
                prev.next = temp.next
  
        # Update Temp for next iteration of outer loop 
                temp = prev.next
                return self.head          
                    
        
            
        
     
a = LinkList()



a.addnode(6)
a.addnode(7)
a.addnode(7)
a.addnode(8)

a.printlist()


