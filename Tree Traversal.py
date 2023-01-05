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

    def BFS(self):
        queue = []
        result = []
        curr_node = self.root
        queue.append(curr_node)
        while len(queue)>0:
            curr_node = queue.pop(0)
            result.append(curr_node.value)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)

        print(result)

    def BFS_preorder(self):
        temp = self.root
        result = []
        nodes = []
        result.append(temp.value)
        while temp.left is not None:
            result.append(temp.left.value)
            temp = temp.left
            if temp.right is not None:
                nodes.append(temp.right)
        while nodes:
            result.append(nodes.pop().value)
        nodes.clear()
        temp = self.root
        result.append(temp.right.value)
        temp = temp.right
        while temp.left is not None:
            result.append(temp.left.value)
            if temp.right is not None:
                nodes.append(temp.right)
            temp = temp.left
        while nodes:
            result.append(nodes.pop().value)
            #if temp.right is not None:
                #temp =temp.right
                #result.append(temp.right.value)
        print(result)

        '''
            if temp.left is not None:
                result.append(temp.left.value)
            if temp.right is not None:
                result.append(temp.right.value)
            temp = temp.left
            print(result)
        while temp.right is not None:
            if temp.left is not None:
                result.append(temp.left.value)
            if temp.right is not None:
                result.append(temp.right.value)
            temp = temp.right
        print(result)'''

    def post_order(self):
        result = []
        def traverse(curr_node):
            if curr_node.left is not None:
                traverse(curr_node.left)
            if curr_node.right is not None:
                traverse(curr_node.right)
            #if curr_node.left is None and curr_node.right is None:
            result.append(curr_node.value)
        traverse(self.root)
        print(result)

    def in_order(self):
        result = []
        def traverse(curr_node):
            if curr_node.left is not None:
                traverse(curr_node.left)
            result.append(curr_node.value)
            if curr_node.right is not None:
                traverse(curr_node.right)
        traverse(self.root)
        print(result)

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


my_tree = BST()
print(my_tree.insert(47))
print(my_tree.insert(21))
print(my_tree.insert(76))
print(my_tree.insert(18))
print(my_tree.insert(27))
print(my_tree.insert(52))
print(my_tree.insert(82))
#my_tree.BFS()
#my_tree.BFS_preorder()
my_tree.post_order()
my_tree.in_order()

