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
        pass

a1=Linklist()
a1.add_begin(10)
a1.add_begin(10)
a1.add_begin(30)
a1.traversal()