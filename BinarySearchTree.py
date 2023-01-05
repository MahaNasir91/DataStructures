class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if temp.value == node.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def print_tree(self):
        temp = self.root
        print(temp.value)
        while temp.left is not None:
            print('/')
            print(temp.left.value)
            temp = temp.left
        temp = self.root
        while temp.right is not None:
            print("\\")
            print(temp.right.value)
            temp = temp.right

    def search(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                return True
        return False

    def min_val(self):
        temp = self.root
        if self.root is None:
            print('Tree is empty')
            return False
        elif temp.left is None:
            return temp.value
        while temp.left is not None:
            temp = temp.left
        return temp.value

my_tree = BST()
print(my_tree.insert(4))
print(my_tree.insert(3))
print(my_tree.insert(5))
print(my_tree.insert(13))
print(my_tree.insert(50))
print(my_tree.insert(31))
print(my_tree.insert(1))
print(my_tree.insert(11))
my_tree.print_tree()
print(my_tree.search(38))
print(my_tree.min_val())