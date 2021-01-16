class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if len(self.items)>0: 
              return self.items.pop()
        else:
              return "No Elements"
    
    def printQueue(self):
        print (self.items)
    

q = Queue()

print("Initialised Queue - Status:")
q.printQueue()

q.enqueue(1)
print("After First Insert Queue - Status:")
q.printQueue()
print("\n")


q.enqueue(2)
print("After Second Insert Queue - Status:")
q.printQueue()
print("\n")

q.enqueue('3')
print("After Third Insert Queue - Status:")
q.printQueue()
print("\n")

q.dequeue()
print("After first Dequeue, Queue - Status:")
q.printQueue()
print("\n")


q.dequeue()
print("After first Dequeue, Queue - Status:")
q.printQueue()
print("\n")


q.dequeue()
print("After first Dequeue, Queue - Status:")
q.printQueue()
print("\n")

q.dequeue()
print("After first Dequeue, Queue - Status:")
q.printQueue()
print("\n")

q.dequeue()
print("After first Dequeue, Queue - Status:")
q.printQueue()
print("\n")
