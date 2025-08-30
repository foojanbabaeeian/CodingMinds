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
        self.head = newNodex