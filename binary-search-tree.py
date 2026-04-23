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

    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)

    def delete(self,data):
        if self.key is None:
            print("Tree is Empty")
        if self.key > data:
            if self.lchild is None:
                print("Not found")
                return
            else:
                self.lchild=self.lchild.delete(data)
        elif self.key < data:
            if self.rchild is None:
                print("Not found")
                return
            else:
                self.rchild=self.rchild.delete(data)
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
    
    def min_search(self):
        if self.key is None:
            print("Tree is Empty")
        elif self.lchild is None:
            print(self.key," is the minimum element in the tree")
        else:
            node=self.lchild
            while node.lchild:
                node=node.lchild
            print(node.key," is the minimum element in the tree")
    
    def max_search(self):
        if self.key is None:
            print("Tree is Empty")
        elif self.rchild is None:
            print(self.key," is the maximum element in the tree")
        else:
            node=self.rchild
            while node.rchild:
                node=node.rchild
            print(node.key," is the maximum element in the tree")

                

#to count no. of nodes in a tree
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.lchild) + count_nodes(node.rchild)


                
root=BST(None)
root.insert(10)
list=[20,5,3,100]
for i in list:
    root.insert(i)
# root.preorder()
# root.inorder()
# if count_nodes(root) > 1:    # to avoid deleting the only node in the tree
#     root.delete(10)
# else:
#     print("Cannot delete the only node in the tree")

root.delete(5)
root.min_search()
root.max_search()
root.postorder()

