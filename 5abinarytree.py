class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def inorder(self):
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

    def preorder(self):
        if self.root is None:
            return

        stack = [self.root]

        while stack:
            current = stack.pop()
            print(current.data, end=" ")

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)


bst = BST()

for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("Inorder:")
bst.inorder()

print("\nPreorder:")
bst.preorder()
