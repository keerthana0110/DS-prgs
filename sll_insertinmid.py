class Node:
    def __init__ (self,data=None):
        self.data=data
        self.next=None
class SLL:
    def __init__ (self):
        self.head=None
        
    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next
    def Inbetween(self,mid_node,newdata):
        if mid_node is None:
            print("the mentioned node is absent")
            return
        temp=Node(newdata)
        temp.next=mid_node.next
        mid_node.next=temp
list=SLL()
list.head=Node("Mon")
e2=Node("Tue")
e3=Node("Thu")
list.head.next=e2
e2.next=e3
list.InBetween(list.head.next,"Fri")
list.listprint()
