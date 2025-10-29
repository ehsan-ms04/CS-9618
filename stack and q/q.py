EMPTYSTRING = ""
NullPointer = -1
MaxQueueSize = 8

FrontOfQueuePointer = 0
EndOfQueuePointer = 0
NumberInQueue = 0
Queue = [EMPTYSTRING for i in range(MaxQueueSize)]

def InitialiseQueue():
    global FrontOfQueuePointer, EndOfQueuePointer, NumberInQueue
    FrontOfQueuePointer = NullPointer 
    EndOfQueuePointer = NullPointer    
    NumberInQueue = 0                  
    print("Queue initialised.")

def AddToQueue(NewItem):
    global EndOfQueuePointer, FrontOfQueuePointer, NumberInQueue, Queue

    if NumberInQueue < MaxQueueSize:
        EndOfQueuePointer = EndOfQueuePointer + 1
        if EndOfQueuePointer > MaxQueueSize - 1:
            EndOfQueuePointer = 0
        Queue[EndOfQueuePointer] = NewItem
        NumberInQueue = NumberInQueue + 1
        if FrontOfQueuePointer == NullPointer:
            FrontOfQueuePointer = 0
        print("Added:", NewItem, "| Queue:", Queue)
    else:
        print("Queue is full")

def RemoveFromQueue():
    global FrontOfQueuePointer, EndOfQueuePointer, NumberInQueue, Queue
    Item = EMPTYSTRING

    if NumberInQueue > 0:
        Item = Queue[FrontOfQueuePointer]
        NumberInQueue = NumberInQueue - 1

        if NumberInQueue == 0:
            InitialiseQueue()
        else:
            FrontOfQueuePointer = FrontOfQueuePointer + 1
            if FrontOfQueuePointer > MaxQueueSize - 1:
                FrontOfQueuePointer = 0

        print("Removed:", Item, "| Queue:", Queue)
    else:
        print("Queue is empty")

    return Item

InitialiseQueue()
AddToQueue("A")
AddToQueue("B")
AddToQueue("C")
RemoveFromQueue()
RemoveFromQueue()
RemoveFromQueue()
RemoveFromQueue()
