#1. Implement “Simple Queue” using list data structure
class SimpleQueue:
    def __init__(self):
        self.data=[]
        self.count=0
    def getElementCount(self):
        return self.count
    def isQueueEmpty(self):
        return self.count==0
    #Adding element to front
    def enqueue(self,ele):
        self.data.append(ele)
        self.count+=1
        return self.count
    #To remove element from rear
    def dequeue(self):
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None
    #To get element at rear
    def peek(self):
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
    def printElements(self):
        return self.data
    
#2. Modify Q1 such that Simple Queue can contain limited amount of elements
class limitedQueue:
    def __init__(self):
        self.count=0
        #Setting the size of the queue
        self.data=[None]*5
        self.front=-1
    def isQueueFull(self):
        return self.count>=len(self.data)#Checking if queue is full
    def isQueueEmpty(self):
        return self.count==0 
    def getCount(self):
        return self.count#Getting the number of elements in queue
    def enqueue(self,element):
        if not self.isQueueFull():#Checking if queue is full
            self.front+=1#if queue is not full then increment the front and enqueue the lement in the index of front
            self.data[self.front]=element
            self.count+=1
            return self.count
        else:
            return None
    def dequeue(self):
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None
    def peek(self):
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
    def printElements(self):
        return self.data

#3. Implement “FlexiQueue”
class FlexiQueue:
    defaultSize=2
    def __init__(self):
        #setting the default size of the queue
        self.data=[None]*FlexiQueue.defaultSize
        self.front=0
        self.count=0
    #Method to get the number of elements in the queue
    def length(self):
        return self.count
    #Method to check if the queue is empty
    def isEmpty(self):
        return self.count==0
    #Method to get the first element in queue
    def getFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
        else:
            return None
    def enqueue(self, ele):
        #Condition to check if the queue is full, if its full resizing the queue
        if self.count==len(self.data):
            self.resize(2*len(self.data))
        idx=(self.front+self.count)%len(self.data)
        self.data[idx]=ele
        self.count+=1
        return self.count
    def dequeue(self):
        if not self.isEmpty():
            ele=self.data[self.front]
            self.count-=1
            self.data[self.front]=None
            #Again shrinking the queue size once deleting the element
            self.front=(self.front+1)%len(self.data)
            if 0<len(self.data)//4:
                self.resize(len(self.data)//2)
            return ele
        else:
            return None
    def resize(self,cap):
        oldData=self.data
        walk=self.front
        self.data=[None]*cap
        for k in range(self.count):
            self.data[k]=oldData[walk]
            walk=(walk+1)%len(oldData)
        self.front=0

    def getSize(self):
        return len(self.data)
    
#4. Implement Stack using two Queues
class stackUsingQueue:
    def __init__(self):
        self.q1=SimpleQueue()
        self.q2=SimpleQueue()
    #enquing the element to queue is same as pushin the element to stack
    def pushNew(self,ele):
        #self.q1.enqueue(ele)
        return self.q1.enqueue(ele)
    #Popping the element from stack should give top element but dequeue operation will give the rear element.
    #So dequeue element from Q1 and enqueue to Q2 until the last elemnt found. The last element is popped. Again all elements from Q2 will be enqued back to Q1
    def popNew(self):
        while(self.q1.getElementCount()>1):
            self.q2.enqueue(self.q1.dequeue())
        ele=self.q1.dequeue()
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.dequeue())
        return ele
    def peekNew(self):
        while(self.q1.getElementCount()>1):
            self.q2.enqueue(self.q1.dequeue())
        ele=self.q1.peek()
        self.q2.enqueue(self.q1.dequeue())
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.dequeue())
        return ele
    
#5. Implement Queue using two Stacks
class queueUsingStack:
    def __init__(self):
        #Initializing 2 stacks
        self.s1=stack()
        self.s2=stack()
    def enqueueNew(self,ele):
        #Enquing to queue is same as pushing the elemnt to stack
        #using the push function used in stack
        self.s1.push(ele)
        return self.s1.count
    def dequeueNew(self):
        #To dequeue an element we need to get the rear element but in stack we can have only top element
        #pop elemnt from stack until we find the last element and push it to new stack S2. the last element from S1 popped will be the front
        #element. Then again from S2 pop element to s1.
        while(self.s1.getCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.pop()
        while(self.s2.getCount()>0):
            self.s1.push(self.s2.pop())
        return ele
    def peekNew(self):
        while(self.s1.getCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.peek()
        self.s2.push(self.s1.pop())
        while(self.s2.getCount()>0):
            self.s1.push(self.s2.pop())
        return ele
    
#6. Write method rotate() which added the existing elements in the reverse order

class Rotate:
    #Contents of queue can be rotated using a stack
    def __init__(self):
        self.q1=SimpleQueue()
        self.s1=stack()
    def rotateMethodUsingStack(self):
        while(self.q1.count>0):
            self.s1.push(self.q1.dequeue())
        while(self.s1.count>0):
            self.q1.enqueue(self.s1.pop())
        return self.q1.printElements()