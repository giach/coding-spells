class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        tmp = Node(data)
        if self.data > data:
            if self.left != None:
                self.left.insert(data)
            else:
                self.left = tmp
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = tmp
            
    def preorder(self):
        print (self.data, end=" ")
        if self.left != None: 
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print (self.data, end=" ")
        if self.right != None:
            self.right.inorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        print (self.data, end=" ")

    def find_val(self, val):
        if self.data > val:
            if self.left != None:
                self.left.find_val(val)
            else:
             print ("the value wasn't found") 
        elif self.data < val:
            if self.right != None:
                self.right.find_val(val)
            else:
                print ("the value wasn't found")
        else:
            print ("the value was found")
        

root = Node(10)
root.insert(5)
root.insert(20)
root.insert(2)
root.insert(7)
root.insert(18)
root.insert(17)

root.preorder()
print ("")
root.inorder()
print ("")
root.postorder()
print ("")

root.find_val(17)
root.find_val(40)
