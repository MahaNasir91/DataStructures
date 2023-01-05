class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if(self.length == 0):
            self.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.head
        while temp is not None:
            if (self.length == 0):
                print('The l.l is empty')
                break

            if(temp.next is None):
                self.head = None
                self.tail = None
                print('The list is now empty')

            if(temp.next == self.tail):
                temp.next = None
                self.tail = temp
                self.length -= 1
            temp = temp.next
        return temp

    def remove(self,index):
        temp = self.head
        if index<0 or index>=self.length:
            print('Index outta range.')
            return None
        elif index == 0:
            self.length -=1
            return self.pop_first()
        elif index == self.length-1:
            self.length -= 1
            return self.pop()
        else:
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next
            temp.next = None
            self.length -=1
            return temp

    def prepend(self,value):
        head = self.head
        new_node = Node(value)

        # If the list is empty
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = head
            self.head = new_node
        self.length+=1
        return True

    def pop_first(self):
        if(self.length==0):
            print('No items to pop as the list is empty.')
            return None
        first_node = self.head

        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = first_node.next
            first_node.next = None
        self.length -=1
        return first_node

    def get(self,index):
        temp = self.head
        ind = 0
        while temp is not None:
            if(ind == index):
                return temp
            temp = temp.next
            ind += 1
        if(index>=self.length-1 or index<0):
            print('Index out of bound.')
            return None

    def set_value(self,index,value):
        temp = self.head
        if index >= self.length:
            print('Index out of bound.')
            return None
        for i in range(index):
            temp = temp.next
        temp.value = value
        return temp.value

    def insert(self,index,value):
        if(index>self.length or index < 0):
            print('Index out of bound')
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedList(4)
my_linked_list.append(value=7)
my_linked_list.append(value=5)
#my_linked_list.print_list()
my_linked_list.prepend(9)
print(my_linked_list.pop_first().value)
print(my_linked_list.pop_first().value)
print(my_linked_list.pop_first())
print(my_linked_list.get(-1))
my_linked_list.set_value(4,4)
my_linked_list.print_list()
my_linked_list.insert(1,8)
my_linked_list.remove(2)
my_linked_list.print_list()
my_linked_list.reverse_list()
my_linked_list.print_list()