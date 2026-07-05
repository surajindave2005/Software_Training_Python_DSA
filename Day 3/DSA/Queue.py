import sys

class Queue:
    def __init__(self, size):
        self.queueSize = size;
        self.myQueue = [];
    
    def enQueue(self, data):
        if(self.isFull()):
            print("******************* Queue is Full **********************");
        else:
            print("Data -> ", data);
            self.myQueue.append(data);

    def deQueue(self):
        if(self.isEmpty()):
            print("******************* Queue is Empty **********************");
        else:
            print("Element deQueue -> ",  self.myQueue.pop(0));
    
    def frontQueue(self):
        if(self.isEmpty()):
            print("Queue is empty ")
        else:
            print("Front Data -> ", self.myQueue[0]);

    def isFull(self):
        if(len(self.myQueue) == self.queueSize):
            return True
        else:
            return False;

    def isEmpty(self):
        if(self.myQueue == []):
            return True
        else:
            return False
        
    def deleteQueue(self):
        del self.myQueue;

    def display(self):
        print("---------------------- DISPLAY ------------------------------")
        if(self.isEmpty()):
            print("-------------- Queue is empty -------------------------");
        else:
            print("Queue -> ", self.myQueue);



print("-------------------------- Queue Operation ----------------------------");

size = int(input("Enter the size of queue: "));
queue = Queue(size);

while True:
    print("1. enQueue")
    print("2. Display")
    print("3. deQueue")
    print("4. Front peek")
    print("5. Delete Queue")
    print("6. Create a Queue")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    print();

    match choice:
        case 1:
            data = int(input("Enter a data : "))
            queue.enQueue(data)

        case 2:
            queue.display();
            print()

        case 3:
            queue.deQueue();
            print()

        case 4:
            queue.frontQueue();
            print()

        case 5:
            queue.deleteQueue();
            print()

        case 6:
            queue = Queue(size);
            
        case 7:
            sys.exit();

        case _:
            print("Invalid operation ")        