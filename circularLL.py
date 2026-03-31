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
            while n is not self.head.ref:
                print(n.data,"--->",end=" ")
                n=n.ref
    
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.ref=self.head
            return
        else:
            n=self.head
            while n is not self.head:
                n=n.ref
            n.ref=new_node
            new_node.ref=self.head
            self.head=new_node

a1=Linklist()
a1.add_begin(10)
a1.traversal()