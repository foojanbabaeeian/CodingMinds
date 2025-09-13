guys = ["Phil", "alvin"]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None

    def push(self,newData):
        newNode=Node(newData)
        newNode.next = self.head
        self.head = newNode

    
    def append(self,newData):
        newNode=Node(newData)
        if self.head is None:
            self.head=newNode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newNode
    def deleteNode(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None
