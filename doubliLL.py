class Node:
    def __init__(self,data):
        self.pref=None
        self.data=data
        self.nref=None

class Linklist:
    def __init__(self):
        self.head=None
    
    def traversal_forward(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.nref

    def traversal_backward(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.pref






    def add_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            self.head.pref=new_node
            new_node.nref=self.head
            self.head=new_node
    
    def add_at_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("Empty List")
        else:
            n=self.head
            while n is not None:
                if n.data == x:
                   break
                n=n.nref
            if n is None:
                ("elemnt not found")
            else:
                new_node.pref=n
                new_node.nref=n.nref
                n.nref=new_node
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node

    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        if self.head.data==x:
            self.head.pref=new_node
            new_node.nref=self.head
            self.head=new_node
            return
        n=self.head
        while n.nref is not None:
            if n.nref.data == x:
                break
            n=n.nref
        if n.nref is None:
            print("element not found")
        else:
            new_node.pref=n
            new_node.nref=n.nref
            n.nref.pref=new_node
            n.nref=new_node

    def add_to_emptyLL(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            print("LL is not empty")
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head.nref.pref=None
            self.head=self.head.nref


    def delete_end(self):
        pass

    def delete_random(self,data):
        pass
            

a1=Linklist() 
a1.add_at_begin(20)
a1.add_at_begin(30)
a1.add_at_last(10)
a1.add_after(40,20)
a1.add_after(50,10)
a1.add_after(90,40)
a1.add_before(60,40)
a1.add_before(70,40)
a1.add_before(80,30)
a1.add_before(90,80)
a1.add_after(90,100)
a1.delete_begin()
a1.delete_begin()
a1.delete_begin()
a1.delete_begin()
a1.traversal_forward() 
# a1.traversal_backward() 

    