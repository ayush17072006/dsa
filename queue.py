class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, ticket):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = ticket

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            print("Booked ticket:", self.queue[self.front])
            self.front += 1

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


q = Queue(5)

q.enqueue("Ticket 101")
q.enqueue("Ticket 102")
q.enqueue("Ticket 103")

q.display()

q.dequeue()
q.display()
