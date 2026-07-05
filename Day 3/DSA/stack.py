# Stack implementation with size limit 
import sys;

class Stack:
    def __init__(self, stackSize):
        self.myStack = [] # list represents stack
        self.stackSize = stackSize; # stack size define
        print("================================ Stack has created ================================")
    
    def push(self, value):
        if(self.isFull()):
            print("***************************** Stack is full ***************************** ");
            
        else:
            print("Data Add: ", value);
            self.myStack.append(value);

    def pop(self):
        if(self.isEmpty()):
            print("***************************** Stack is underflow ***************************** ")
        else:
            print("***************************** Element poped *****************************  ");
            print("Element poped: ", self.myStack.pop());
            # alternative way self.myStack[-1]

    def peek(self):
        if(self.isEmpty()):
            print("*****************************  Stack is underflow ***************************** ");
        else:
            self.peekData = self.myStack[-1];
            print("Peek Data = ", self.peekData);
    
    def isFull(self):
        if(len(self.myStack) == self.stackSize):
            return True;
        else:
            return False;

    def isEmpty(self):
        if(self.myStack == []): # alternative way if(self.mystack == [])
            return True
        else:
            return False
    
    def display(self):
        if(self.isEmpty()): 
            print("***************************** Stack is empty ***************************** ");
        else:
            print(self.myStack);
    def delete(self):
        print("********************* Stack is Deleted **************************")
        del self.myStack;
        # alternative way
        


print("****************************** Welcome to the Stack Menu Driven *******************************  ")
size = int(input("Enter a stack size: "))

obj = Stack(size);
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Delete")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if(choice==1):
        data = int(input("Enter a value to push in stack: "))
        obj.push(data);
        print("**************************************************************************")
        print();
    
    elif(choice==2):
        obj.pop();
        print("**************************************************************************")
        print();
    
    elif(choice==3):

        obj.peek();
        print("**************************************************************************")
        print();
    
    elif(choice==4):
        print("**************************************************************************")
        obj.display();
        print();
    
    elif(choice==5):
        obj.delete();
    elif(choice==6):
        print("************************** Thank you for Visiting *************************************")
        sys.exit();
    else:
        print("Please enter valid operation ")


