class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        node = Node(value)
        self.last = node
        self.first = node
        self.length = 1

    def enqueue(self,value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return True

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def dequeue(self):
        temp = self.first
        if self.length == 0:
            print('Empty Queue')
            return None
        elif self.length == 1:
            self.last = None
            self.first = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp

my_q = Queue(6)
my_q.enqueue(4)
my_q.dequeue()
my_q.print_queue()