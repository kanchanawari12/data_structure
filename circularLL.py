# singly LL
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linklist:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while True:
                print(n.data,"--->",end=" ")
                n=n.ref
                if n==self.head:
                    break
    
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=new_node
            self.head=new_node
            return
        else:
            n=self.head
            while n.ref != self.head:
                n=n.ref
            new_node.ref=self.head
            self.head=new_node
            n.ref=self.head
        
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=new_node
            self.head=new_node
            return
        else:
            n=self.head
            while n.ref != self.head:
                n=n.ref
            n.ref=new_node
            new_node.ref=self.head

    def add_after(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("LL is empty")
            return
        elif self.head.ref==self.head and self.head.data==x:
            self.head.ref=new_node
            new_node.ref=self.head
        else:
            n=self.head
            while True:
                if n.data==x:
                    new_node.ref=n.ref
                    n.ref=new_node  
                    return  
                n=n.ref
                if n==self.head:
                    print("Element not found")
                    break
                
            
            
            
a1=Linklist()
a1.add_begin(10)
a1.add_begin(10)
a1.add_begin(30)
a1.add_end(40)
a1.add_end(50)
a1.add_after(70,0)
a1.add_after(20,50)
a1.add_after(60,40)
a1.traversal()