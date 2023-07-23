#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:30:36 2023

@author: prashantsingh
"""

# source https://leetcode.com/problems/lru-cache/

from collections import defaultdict


class LRUCache:
    """Implementation 1.  - NOT OPTIMAL SOLUTION (Not Complete)
    ---------------------------------------------------------------------------
    Data Structures -
    -----------------
    Recency_counter : a proxy of timestamp(always increasing)
        
    lru -> {key: value} => {3:300, 4:400, 5:500}
    recency -> {key: time_counter} => {3:1, 4:2, 5:3}
    
    ---------------------------------------------------------------------------
    
    Create a dictionary recency, which will record the timestamp when an item was
    used last time.
    
    put() -> if cache is full, scan `recency` dictionary and find item with 
    lowest timestamp. Remove it from recency and lru dictionary. Add new item 
    with new recency value in recency and update item in lru
    
    ---------------------------------------------------------------------------
    Time Complexity - 
        put() -> O(n) for finding the last recently used item in recency dict.
        get() -> O(1)
        
    Space Complexity - 
        O(n) -> for storing recency values.
     ---------------------------------------------------------------------------
     TODO -
         1. Update the lru if key already available in put(k,v)
    
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.recency = {}
        self.recency_counter = 0

    def get(self, key: int) -> int:
        try:
            val = self.lru[key]
            self.recency_counter += 1
            self.recency[key] = self.recency_counter
            return val
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lru) == self.capacity:
            min_recency_key = self.__find_min_recencey_key()
            del self.recency[min_recency_key]
            del self.lru[min_recency_key]
            self.lru[key] = value
            self.recency_counter += 1
            self.recency[key] = self.recency_counter

        else:
            self.lru[key] = value
            self.recency_counter += 1
            self.recency[key] = self.recency_counter

    def __find_min_recencey_key(self) -> int:
        min_value = min(self.recency.values())
        min_key = [key for key in self.recency if self.recency[key] == min_value]
        return min_key[0]

    def __str__(self):
        return str(self.lru) + " - " + str(obj.recency)

    def __repr__(self):
        return str(self.lru) + " - " + str(obj.recency)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
param_1 = obj.get(1)
obj.put(20, 200)
obj.put(30, 300)
obj.put(40, 400)
obj.put(50, 500)


# %%
""" Implementation 2: Optimal Solution, ACCEPTED ANSWER
    ---------------------------------------------------------------------------
    Data Scructures- 
        Node 
            - key,value
            
        DoublyLinkedList 
            - head is least recently used item, tail is last used.
            - Every time new item is added, add it after tail.
            - If size is greater than capacity, move head one step ahead.
            - Every time a node is accessed, move it at the end of doubly LL.
        
        lookup_hash
            - in order to search item from doubly linked list, we will need to 
            travese the whole linked list. O(n)
            To avoid this, we can use this lookup_hash. 
            key is key of node, and value is actual refrence to node.
            {3: Node(3,400), }
    
    ---------------------------------------------------------------------------
    Time Complexity 
        put(k,v) -> )(1)
        get(k) -> O(1)
    
    Space Complexity:
        O(n) to create lookup_hash
    ---------------------------------------------------------------------------

"""
class Node:
    def __init__(self, key, value, next=None, previous=None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return f"[{self.key}:{self.value}] <==>"

    def __repr__(self):
        return f"[{self.key}:{self.value}] <==>"


class DoublyLL:
    def __init__(self, head: Node):
        self.head = head
        self.tail = self.head
        self.head.next = head
        self.head.previous = head
        self.len = 1

    def add_node_at_end(self, n: Node):

        self.tail.next = n
        n.previous = self.tail
        n.next = self.head
        self.head.previous = n
        self.tail = n
        #self.len += 1

    def move_head(self):
        """Moves Head of DLL to one step.
        """
        self.head.next.previous = self.head.previous
        self.head = self.head.next
        self.tail.next = self.head

    def move_node_at_end(self, n: Node):
        if self.head == n:      # if node is a head
            self.move_head()    # move head to next
        elif self.tail == n:  # if node is a tail
            return             # do nothing because it's already at end
            
            
        # remove this node from list
        n.previous.next = n.next
        n.next.previous = n.previous
        #self.len -= 1

        # add this node at end
        self.add_node_at_end(n)

        if n == self.head:
            self.head = self.head.next

    def __repr__(self):
        return str(self)

    def __str__(self):
        pt = self.head
        x = ""
        i = 10
        while pt != self.tail:
            x += str(pt)
            i += 1
            pt = pt.next
            if i == 10:
                pass
        x += str(pt)
        return x


class LRUCache:

    def __init__(self, capacity: int):
        self.dll = None
        self.capacity = capacity
        self.lookup_hash = dict()  # to fecilitate searching in O(1)

    def get(self, key: int) -> int:
        try:
            node = self.lookup_hash[key]
            # Now shift this node to end of DLL
            self.dll.move_node_at_end(node)
            #print(f"{self.dll} _{self.dll.len}_")
            #print("-.-"*10)
            return node.value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            node = self.lookup_hash[key]  # key is already available
            node.value = value               # update node's value
            self.dll.move_node_at_end(node)  # move node at end
            return                           # don't do anything else
        except KeyError:
            pass

        n = Node(key, value)              # create new node
        self.lookup_hash[key] = n         # register it in lookup

        if self.dll is None:            # First node. 
            self.dll = DoublyLL(head=n) # Make it head of DoublyLL.

        elif self.dll.len < self.capacity:  # Not Full. 
            self.dll.add_node_at_end(n)     # Keep appending at end
            self.dll.len+=1                 # increase length
        
        else:                               # Full
            self.dll.add_node_at_end(n)      # Add at last positionn.
            # delete head-key from lookup
            del self.lookup_hash[self.dll.head.key]
            self.dll.move_head()             # Shift head to next.


        #print(f"{self.dll} _{self.dll.len}_ :: {self.lookup_hash}")
        #print("--"*10)

#%%
obj = LRUCache(5)
obj.put(10,100)
obj.put(20, 200)
obj.put(30, 300)
obj.put(40, 400)
obj.put(50, 500)
obj.put(60, 600)
obj.get(40)
obj.put(60,601)
#obj.get(20)

# %%

obj = LRUCache(1)
obj.put(2,0)
obj.get(2)