from collections import deque

que1 = [] #create emptyy list

def enqueue (queue, value): #define enqueue
    queue.append(value)

def dequeue (queue): #define dequeue
    queue.pop(0)


enqueue(que1,27)
enqueue(que1,15) #add values to thr que
enqueue(que1,22)

print(que1) #print queue

dequeue(que1) #remove head value

print(que1) #print queue

enqueue(que1,2776)

print(que1)
