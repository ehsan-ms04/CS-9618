
emptystring = ""
nullpointer = -1
maxstacksize = 8

basestackpointer = 0
topstackpointer = 0
Stack = [emptystring for i in range(maxstacksize)]

def initialisestack():
    global basestackpointer, topstackpointer
    basestackpointer = 0             
    topstackpointer = nullpointer    
    print("Stack initialised.")

def Push(NewItem):
    global topstackpointer, Stack
    if topstackpointer < maxstacksize - 1:
        topstackpointer = topstackpointer + 1
        Stack[topstackpointer] = NewItem
        print("Pushed:", NewItem, "| Stack:", Stack)
    else:
        print("Stack Overflow!")

def Pop():
    global topstackpointer, Stack
    Item = emptystring
    if topstackpointer > nullpointer:
        Item = Stack[topstackpointer]
        topstackpointer = topstackpointer - 1
        print("Popped:", Item, "| Stack:", Stack)
    else:
        print("Stack Underflow!")
    return Item

# test run
initialisestack()
Push("A")
Push("B")
Push("C")
Pop()
Pop()
Pop()
Pop()
