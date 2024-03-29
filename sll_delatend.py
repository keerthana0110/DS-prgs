class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None 
def push(head, data): 
	if not head: 
		return Node(data) 
	temp = Node(data) 
	temp.next = head 
	head = temp 
	return head 
 
def removeLastNode(head): 
	if head == None: 
		return None
	if head.next == None: 
		head = None
		return None
	second_last = head 
	while(second_last.next.next): 
		second_last = second_last.next
	second_last.next = None
	return head 

if __name__=='__main__': 
 
	head = None
	head = push(head, 12) 
	head = push(head, 29) 
	head = push(head, 11) 
	head = push(head, 23) 
	head = push(head, 8) 

	head = removeLastNode(head) 
	while(head): 
		print("{} ".format(head.data), end ="") 
		head = head.next

