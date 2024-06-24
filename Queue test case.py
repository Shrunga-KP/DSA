from queue import *


#1. Simple Queue
def testEmptyQueue():
    s1=SimpleQueue()
    assert(s1.getElementCount()==0)
    assert(s1.isQueueEmpty()==True)

def testEnqueue():
    s2=SimpleQueue()
    s2.enqueue(10)
    assert(s2.getElementCount()==1)
    assert(s2.peek()==10)

def testDequeue():
    s3=SimpleQueue()
    s3.enqueue(20)
    s3.enqueue(30)
    s3.enqueue(40)
    assert(s3.getElementCount()==3)
    assert(s3.peek()==20)
    assert(s3.dequeue()==20)
    assert(s3.getElementCount()==2)
    assert(s3.printElements()==([30,40]))

testEmptyQueue()
testEnqueue()
testDequeue()

#2. limited amount of elements
def testEmptyQueue():
    s1=limitedQueue()
    assert(s1.getCount()==0)
    assert(s1.isQueueEmpty()==True)
    assert(s1.isQueueFull()==False)

def testEnqueue():
    s2=limitedQueue()
    s2.enqueue(10)
    assert(s2.getCount()==1)
    assert(s2.peek()==10)

def testDequeue():
    s3=limitedQueue()
    s3.enqueue(20)
    s3.enqueue(30)
    s3.enqueue(40)
    s3.enqueue(50)
    s3.enqueue(60)
    assert(s3.isQueueFull()==True)
    assert(s3.getCount()==5)
    assert(s3.peek()==20)
    assert(s3.dequeue()==20)
    assert(s3.getCount()==4)
    assert(s3.printElements()==([30,40,50,60]))

testEmptyQueue()
testEnqueue()
testDequeue()

#3.
from flexiQueue import *
def testEmptyQueue():
    s1=FlexiQueue()
    assert(s1.length()==0)
    assert(s1.isEmpty()==True)

def testEnqueue():
    s2=FlexiQueue()
    s2.enqueue(10)
    assert(s2.length()==1)

def testDequeue():
    s3=FlexiQueue()
    assert(s3.getSize()==2)
    s3.enqueue(20)
    s3.enqueue(30)
    assert(s3.getSize()==2)
    s3.enqueue(40)
    assert(s3.getSize()==4)
    assert(s3.dequeue()==20)
    assert(s3.length()==2)
    assert(s3.dequeue()==30)
    assert(s3.getSize()==2)
testEmptyQueue()
testEnqueue()
testDequeue()

#4.s1=stackUsingQueue()
assert(s1.pushNew(10)==1)
assert(s1.pushNew(20)==2)
assert(s1.pushNew(30)==3)
assert(s1.popNew()==30)
assert(s1.peekNew()==20)

#5.  Queue using two Stacks
q1=queueUsingStack()
assert(q1.enqueueNew(10)==1)
assert(q1.enqueueNew(20)==2)
assert(q1.enqueueNew(30)==3)
assert(q1.dequeueNew()==10)
assert(q1.peekNew()==20)

#6.

q=Rotate()
q.q1.enqueue(10)
q.q1.enqueue(20)
q.q1.enqueue(30)
q.q1.enqueue(40)
assert(q.rotateMethodUsingStack()==([40,30,20,10]))