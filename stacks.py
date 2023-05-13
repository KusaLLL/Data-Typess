stack = [] # create empty list

stack.append(1)
stack.append(2) #append (insert) values to the empty list 1 by one
stack.append(3)

print(stack.pop())

def push (stack,value):
    stack.append(value) # define psuh 

def pop (stack):
    return stack.pop() # define pop 


push(stack, 45) # insert values to the stack using push command
push(stack, 55)
print(stack)

print(stack.pop()) # one way to delete a value

pop(stack)
print(stack) # 2nd way to delete a value





