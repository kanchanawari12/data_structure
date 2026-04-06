class BST:
    def __init__(self,key):
        self.lchild=None
        self.key=key
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key > data:
            if self.lchild is None:
                self.lchild=BST(data)
                return
            else:
                self.lchild.insert(data)
            
        else:
            if self.rchild is None:
                self.rchild=BST(data)
                return
            else:
                self.rchild.insert(data)


    def search(self,data):
        if self.key is None:
            print("Tree is Empty")
        if self.key == data:
            print("found")
            return
        if self.key > data:
            if self.lchild is None:
                print("Not found")
                return
            else:
                self.lchild.search(data)
        else:
            if self.rchild is None:
                print("Not found")
                return
            else:
                self.rchild.search(data)

root=BST(None)
root.insert(10)
list=[1,5,15,20,3]
for i in list:
    root.insert(i)
root.search(21)