# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:29:47 2021

@author: Abeg
"""
#Doubly Linkedlist
import gc
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
  

class DoublyLinkedList: 
  
    
    def __init__(self): 
        self.head = None
  
    
    def push(self, new_data): 
  
       
        new_node = Node(new_data) 
  
        
        new_node.next = self.head 
  
        
        if self.head is not None: 
            self.head.prev = new_node 
  
        
        self.head = new_node 
  
    
    def insertAfter(self, prev_node, new_data): 
  
        
        if prev_node is None: 
            print("the given previous node cannot be NULL")
            return 
  
       
        new_node = Node(new_data) 
  
        
        new_node.next = prev_node.next#imp
  
        
        prev_node.next = new_node 
  
        
        new_node.prev = prev_node 
  
       
        if new_node.next is not None: 
            new_node.next.prev = new_node 
  
    
    def append(self, new_data): 
  
        
        new_node = Node(new_data) 
  
         
        new_node.next = None
  
        
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
  
        
        last = self.head 
        while(last.next is not None): #imp
            last = last.next
  
         
        last.next = new_node 
  
       
        new_node.prev = last 
  
        return
    
    def deleteNode(self, dele):
         
        
        if self.head is None or dele is None:
            return
         
        
        if self.head == dele:
            self.head = dele.next
 
        
        if dele.next is not None:
            dele.next.prev = dele.prev
     
        
        if dele.prev is not None:
            dele.prev.next = dele.next
        
        gc.collect()
  
   
    def printList(self, node): 
  
        print("\nTraversal in forward direction")
        while(node is not None): 
            print(" % d" %(node.data)) 
            last = node 
            node = node.next
  
        print("\nTraversal in reverse direction")
        while(last is not None): 
            print(" % d" %(last.data))
            last = last.prev 


    
  
# Driver program to test above functions 
  
# Start with empty list 
dllist = DoublyLinkedList() 
# Insert 6. So the list becomes 6->None 
dllist.append(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
dllist.push(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
dllist.push(1) 
dllist.append(4) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
print("original list")
print(dllist.printList(dllist.head))
dllist.deleteNode(dllist.head)
#dllist.deleteNode(dllist.head.next)
print("modifiedlist")
print(dllist.printList(dllist.head))
