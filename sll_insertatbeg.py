class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next
    def AtBeg(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
list=SLinkedList()
list.head=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.head.next=e2
e2.next=e3
list.AtBeg("Sun")
list.listprint()
