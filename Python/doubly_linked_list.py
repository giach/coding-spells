class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.nxt = None



class DoublyLinkedList:
	def __init__(self):
		self.begin = None
		self.end   = None

	def push(self, node):

		if self.begin is None:
			self.begin = self.end = node

		elif self.begin == self.end:
			self.end = node
			self.end.prev = self.begin
			self.begin.nxt = self.end

		else:
			self.end.nxt = node
			node.prev = self.end
			self.end = self.end.nxt

	def print(self):
		node = self.begin

		while node:
			print(node.val, end = " ")
			node = node.nxt
		print("")



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

dlist = DoublyLinkedList()

dlist.push(n1)
dlist.push(n2)
dlist.push(n3)
dlist.push(n4)
dlist.push(n5)

dlist.print()