class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_node(head, node):
    if head is None:
        head = node
        return head

    new_tree = head
    while head.next is not None:
        head = head.next

    head.next = node
    return new_tree


def serialize(head, c):
    if head is None:
        return ""

    strtree = head.val + "|" + c + "|" +  serialize(head.left,"l") +  serialize(head.right,"r")
    return strtree

def deserialize(stree):
    ltree = stree.split("|")
    print ltree
    for n in ltree:
        print n
    

node = Node('root', Node('left', Node('left.left')), Node('right'))
stree = serialize(node, "r")
print stree

deserialize(stree)
