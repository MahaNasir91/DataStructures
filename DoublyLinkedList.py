class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
        self.length += 1

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if (self.length == 0):
            print('Cant pop cx the list is empty')
            return None
        elif (self.length == 1):
            temp = self.head
            self.head = None
            self.tail = None
            print ('The list is now empty.')
        else:
            temp = self.tail
            pre = temp.prev
            self.tail = pre
            pre.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def prepend(self,value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return new_node.value

    def pop_first(self):
        temp = self.head
        if(self.length == 0):
            print('No item to pop cx l.l empty')
            return None
        elif(self.length == 1):
            self.head = None
            self.tail = None
        else:
            next_node = self.head.next
            self.head = next_node
            temp.next = None
            next_node.prev = None
        self.length -=1
        return temp

    def get(self,index):
        if (index<0 or index>=self.length):
            print('Index outta range')
            return None
        temp = self.head
        #We do this only if the index is in the first half of the ll
        if(index < self.length/2):
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1 , index, -1):
                temp = temp.prev
        return temp

    def set_value(self,index,value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False

    def insert(self,index,value):
        node = Node(value)
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif index<0 or index>self.length:
            print('get lost')
            return None
        else:
            curr_node = self.get(index)
            pre_node = curr_node.prev
            node.next = curr_node
            pre_node.next = node
            node.prev = pre_node
            curr_node.prev = node
            self.length += 1
            return True

    def remove(self,index):
        curr_node = self.get(index)
        if curr_node is None:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length -1:
            return self.pop()
        elif self.length == 0:
            print('List is empty')
            return None
        elif self.length == 1:
            curr_node.next = None
            curr_node.prev = None
        else:
            pre = curr_node.prev
            after = curr_node.next
            pre.next = after
            after.prev = pre
            curr_node.next = None
            curr_node.prev = None
        self.length -= 1
        return curr_node


my_dlist = DoublyLinkedList(4)
my_dlist.append(7)
my_dlist.append(5)
my_dlist.append(9)
my_dlist.pop()
my_dlist.prepend(2)
my_dlist.pop_first()
print(my_dlist.get(2))
my_dlist.set_value(2,8)
my_dlist.insert(3,9)
my_dlist.remove(0)
my_dlist.print_list()