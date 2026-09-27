class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Deleted:", self.head.data)
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


l = LinkedList()

l.insert_beginning("Python")
l.insert_beginning("C++")
l.insert_end("Java")

l.display()

l.delete_beginning()

l.display()
