# traversal operation of linked list

# node class is used to create new node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Link_list:
    def __init__(self):
        self.head=None           # initially head is none
        
    def traver_operation(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n is not None:
               print(n.data,"----->",end=" ")
               n=n.ref

    def add_at_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node                # assign value when while condition become false

    def addinbetween_after(self,data,x):
        new_node=Node(data)
        n=self.head
        # this is one way
        # while n is not None:
        #     if n.data == x:
        #         new_node.ref=n.ref
        #         n.ref=new_node
        #         break
        #     n=n.ref
        # if n is None:
        #     print("item not found in LL")
        # else:

        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Item not found Error")
        else:
            new_node.ref=n.ref
            n.ref=new_node

    def addinbetween_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data==x:
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref
        if n.ref is None:
            print("Item not found")
        else:
            new_node.ref=n.ref
            n.ref=new_node

    def adddata_toemptyLL(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=self.head
            self.head=new_node
        else:
            print("LL is not empty")
        

            
        

a=Link_list()
a.adddata_toemptyLL(10)
a.traver_operation()
    
    
  
