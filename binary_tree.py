

class Node:
    def __init__(self,data,right=None,left=None):
        self.data = data
        self.left = left
        self.right = right
        
class BST : 
    def __init__(self):
        self.root= None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else :
            self._insert(self.root,data)

    def _insert(self,root,data):
        if data < root.data :
            if root.left is None:
                root.left = Node(data)
            else :
                self._insert(root.left,data)

        elif data > root.data :
            if root.right is None :
                root.right = Node(data)
            else :
                self._insert(root.right,data)

    def preorder(self,root):
        if not root :
            return
        print(root.data)

        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if not root :
            return
        

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def inorder(self,root):
        if not root :
            return
        

        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        

    def search(self,root , target):

        if not root :
            return False
        
        if root.data == target :
            return print(True)
        
        if target > root.data :
            return self.search(root.right,target)

        else :
        
            return self.search(root.left,target)


keys = [10,43,20,5,4,8,9,90]
bst = BST()

for k in keys :
    bst.insert(k)

bst.inorder(bst.root)

bst.search(bst.root,90)