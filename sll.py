class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insertAtBeg(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    
    def delAtBeg(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None
    
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"==>",end='')
            temp=temp.next
        print("None")
obj=SLL()
ch=0
while ch!=4:
    print("linked list implementation\n","1.Insertion at beginning 2.deletion 3.print list 4.exit")
    ch=int(input())
    if ch==1:
        print("enter the value of node")
        data=input()
        obj.insertAtBeg(data)
        obj.printlist()
    elif ch==2:
        obj.delAtBeg()
        obj.printlist()
    elif ch==3:
        obj.printlist()

