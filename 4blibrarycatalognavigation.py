class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LibraryTree:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


root = Node("Library")
root.left = Node("Science")
root.right = Node("Arts")
root.left.left = Node("Physics")
root.left.right = Node("Computer Science")
root.right.left = Node("History")
root.right.right = Node("Literature")

tree = LibraryTree()

print("Inorder:")
tree.inorder(root)

print("\nPreorder:")
tree.preorder(root)

print("\nPostorder:")
tree.postorder(root)
