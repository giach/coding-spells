class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, data):
        self.queue.insert(0, data)

    def remove(self):
        self.queue =  self.queue[1:]
    def poll(self):
        self.queue.pop()
    def peek(self):
        return self.queue[len(self.queue)-1]

    def printq(self):
        print(self.queue)

q = Queue()

q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)

q.printq()

q.remove()
q.printq()

q.poll()
q.printq()

print(q.peek)


