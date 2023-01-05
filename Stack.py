class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_queue(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        node = Node(value)
        if self.height >= 1:
            node.next = self.top
        self.top = node
        self.height += 1
        return node

    def pop(self):
        temp = self.top
        if self.height == 0:
            print('No items to pop as the stack is empty')
            return None
        elif self.height == 1:
            self.top = None
            print('The stack is now empty')
        else:
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp


my_stack = Stack(7)
my_stack.push(4)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.push(8)
my_stack.push(4)
my_stack.push(1)
my_stack.print_queue()