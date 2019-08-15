class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def AtEnd(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=temp
    def listprint(self):
       printval=self.head
       while printval is not None:
           print(printval.data)
           printval=printval.next
list=SLinkedList()
list.head=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.head.next=e2
e2.next=e3
list.AtEnd("Thu")
list.listprint()
