class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.left = None
        self.right = None


class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, roll, name):
        new_node = Node(roll, name)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if roll < temp.roll:
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
            print(current.roll, current.name)
            current = current.right

    def preorder(self):
        if self.root is None:
            return

        stack = [self.root]

        while stack:
            current = stack.pop()
            print(current.roll, current.name)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)


bst = StudentBST()

bst.insert(105, "Rahul")
bst.insert(101, "Amit")
bst.insert(110, "Priya")
bst.insert(103, "Neha")
bst.insert(108, "Riya")
bst.insert(115, "Arjun")

print("Inorder:")
bst.inorder()

print("\nPreorder:")
bst.preorder()
