class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LL:
    def __init__(self):
        self.head=None

    def traverse(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"---->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        n=self.head
        while n is not None:
            n=n.ref
        n.ref=new_node

    def add_between_after(self,data,x):
        new_node=Node(data)
        n=self.head
        while n is not None:
            if n.data==x:
               break
            n=n.ref
        if n is None:
            print("Element not found")
        else:
             new_node.ref=n.ref
             n.ref=new_node

    def add_betweeen_before(self,data,x):
        new_node=Node(data)
        if self.head.data==x:
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n is None:
            print("Item not exist")
        else:
            new_node.ref=n.ref
            n.ref=new_node

    def remove_frombegin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head=self.head.ref

    def remove_fromend(self):
        if self.head is None:
            print("empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while True:
                if n.ref.ref is None:
                    n.ref=None
                    return
                n=n.ref

    def delete_random_node(self,x):
        if self.head is None:
            print("empty")
        else:
            if self.head.data == x:
                self.head=self.head.ref
            else:
                n=self.head
                while n is not None:
                    if n.ref.data == x:
                        n.ref=n.ref.ref
                        return
                    n=n.ref
                if n is None:
                    print("Item Not found")

    def delete_random_after(self,x):
        if self.head.ref is None:
            print("Only one Node present")
            return
        n=self.head
        while n is not None:
            if n.data==x:
               if n.ref is None:
                   print("Last node")
                   return
               n.ref=n.ref.ref
            n=n.ref

    # def delete_random_before(self,x):
    #     if self.head.ref is None or self.head is None:
    #         print("Not enough Node")
    #         return
    #     prev = None
    #     n=self.head
    #     while n is not None:
    #         if n.ref.data == x:
    #             prev=n.ref
    #             return
    #         n=n.ref
    #     while True:
    #         if n.ref.ref == prev:
    #             n.ref=prev
    #             return
    #         n=n.ref
            
b1=LL()
b1.add_begin(10)
b1.add_begin(20)
b1.add_begin(30)
b1.add_between_after(0,10)
b1.add_betweeen_before(40,30)
b1.add_betweeen_before(60,40)
b1.add_between_after(50,60)
b1.add_betweeen_before(2,30)
b1.delete_random_node(2)
b1.delete_random_node(0)
b1.delete_random_after(30)
b1.delete_random_after(50)
b1.traverse()

