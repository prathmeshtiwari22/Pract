def find_pair(nums,target):
    flag=0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                print("pair found  ",nums[i],nums[j])
                flag+=1
    if flag==0:
        print("pair not found")
    #print("pair not found")
nums = [5,2,6,8,1,9]
target= 12

find_pair(nums,target)

APPROACH 2:
def find_pair(nums,target):
    nums.sort()
    low=0
    high=len(nums)-1
    ans=[]
    while low< high:
        if nums[low]+nums[high]==target:
            ans.append((nums[low],nums[high]))
        if nums[low] + nums[high] <target:
            low+=1
        else:
            high-=1
    if len(ans)==0:
        print("pair not found")
    else:
        print(ans)
            
nums = [5,2,6,8,1,9]
target= 10

find_pair(nums,target)

FOR THREE :
def find_pair(nums, target):
    nums.sort()
    ans=[]
    
    for i in range(0,len(nums)-1):
        low=i+1
        high=len(nums)-1
        
        while low<high:
            sums=nums[i]+nums[low]+nums[high]
            if sums== target:
                ans.append([nums[i],nums[low],nums[high]])
            if sums<target:
                low+=1
            else:
                high-=1
                
    if len(ans) ==0:
        print(" pair not found \n")
    else:
        print(ans)

nums = [2, 7, 4, 0, 9, 5, 1, 3]
target = 6

find_pair(nums, target)
APPROACH: def isTripletExist(nums,target,count,n):
    if count==3 and target ==0:
        return True
    
    if count==3 or n==0 or target <0:
        return False
    
    return isTripletExist(nums,target-nums[n-1],count+1,n-1) or isTripletExist(nums,target,count,n-1)

nums = [2, 7, 4, 0, 9, 5, 1, 3]
target = 6

if isTripletExist(nums,target,0,len(nums)):
    print("yes")
else:
    print("NO")


BST PAIR APPROACH: class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


root = None

data_list = [15, 10, 20, 8, 12, 16, 25]
for data in data_list:
    root = insert(root, data)


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

print("Inorder Traversal:")
inorder_traversal(root)
print("\n")


def find_pair(root, target, s):
    if root is None:
        return False

    # Traverse the left subtree
    if find_pair(root.left, target, s):
        return True

    # Check if the complement (target - root.data) exists in the set
    if target - root.data in s:
        print(f"Pair found: ({target - root.data}, {root.data})")
        return True
    else:
        s.add(root.data)

    # Traverse the right subtree
    return find_pair(root.right, target, s)


target_sum = 28
s = set()
if not find_pair(root, target_sum, s):
    print("No pair found.")
APPROACH: class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


root = None

data_list = [15, 10, 20, 8, 12, 16, 25]
for data in data_list:
    root = insert(root, data)


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

print("Inorder Traversal:")
inorder_traversal(root)
print("\n")


def find_pair(root, target, s):
    if root is None:
        return False

    if find_pair(root.left, target, s):
        return True

    if target - root.data in s:
        print(f"Pair found: ({target - root.data}, {root.data})")
        return True
    else:
        s.add(root.data)

    return find_pair(root.right, target, s)


target_sum = 28
s = set()
if not find_pair(root, target_sum, s):
    print("No pair found.")
LINKEDLIST: 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next= next

class LinkedList:
    def __init__(self):
        self.head=None
        
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("NULL ")

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next= self.head
        self.head=new_node

    def insert_at_end(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        

        
    def insert_after_node(self,prev_node_data,data):
        temp = self.head
        while temp:
            if temp.data == prev_node_data:
                new_node=Node(data)
                new_node.next=temp.next
                temp.next=new_node
                return
            temp=temp.next
        print(f"Node with data {prev_node_data} not found.") 
 

if __name__ == "__main__":
    llist = LinkedList()


    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    print("Linked List after inserting 1, 2, 3:")
    llist.print_list()


    llist.insert_at_start(0)
    print("Linked List after inserting 0 at the start:")
    llist.print_list()

   
    llist.insert_after_node(2, 2.5)
    print("Linked List after inserting 2.5 after 2:")
    llist.print_list()

 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next= next

class LinkedList:
    def __init__(self):
        self.head=None
        
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("NULL ")

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next= self.head
        self.head=new_node

    def insert_at_end(self, data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        

        
    def insert_after_node(self,prev_node_data,data):
        temp = self.head
        while temp:
            if temp.data == prev_node_data:
                new_node=Node(data)
                new_node.next=temp.next
                temp.next=new_node
                return
            temp=temp.next
        print(f"Node with data {prev_node_data} not found.")
    
    def deleteL(self,key):
        temp=self.head
        if temp and temp.data == key:
            self.head=temp.next
            temp=None
            return
        prev= None
        while temp and temp.data != key:
            prev=temp
            temp=temp.next
        if not temp:
             print(f"Node with data {key} not found.")
             return
        prev.next=temp.next
        temp=None
            
            
 
 
 

if __name__ == "__main__":
    llist = LinkedList()


    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    print("Linked List after inserting 1, 2, 3:")
    llist.print_list()


    llist.insert_at_start(0)
    print("Linked List after inserting 0 at the start:")
    llist.print_list()

   
    llist.insert_after_node(2, 2.5)
    print("Linked List after inserting 2.5 after 2:")
    llist.print_list()

    llist.deleteL(2)
    print("Linked List after inserting 2.5 after 2:")
    llist.print_list()


