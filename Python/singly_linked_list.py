class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if not self.head:
            self.head = node
            return

        tmp = self.head

        while tmp.next:
            tmp = tmp.next

        tmp.next = node

    def del_node(self, value):
        tmp = self.head
    
        if tmp.value == value:
            self.head = head.next
            return
        
        while tmp.next:
            if tmp.next.value == value:
                break
            tmp = tmp.next

        tmp.next = tmp.next.next

    def print(self):
        tmp = self.head

        while tmp:
            print(tmp.value, " ", end="")
            tmp = tmp.next
        print()

    def remove_duplicates(self):

        p1 = self.head
        p2 = self.head

        while p1.next:
            while p2.next:
                if p1.value == p2.next.value:
                    p2.next = p2.next.next
                p2 = p2.next if p2.next else p2
            p1 = p1.next



def main():
    tmp1 = Node(1)
    tmp2 = Node(2)
    tmp3 = Node(3)
    tmp4 = Node(4)

    s = SinglyLinkedList()

    #s.add_node(Node(3))
    s.add_node(tmp1)
    s.add_node(tmp2)
    s.add_node(tmp3)
    s.add_node(tmp4)
    s.add_node(Node(3))
    s.add_node(Node(5))
    s.add_node(Node(3))
    s.print()

    # s.del_node(3)
    s.remove_duplicates()

    s.print()
main()
