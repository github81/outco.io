
"""
https://www.hackerrank.com/test/d6aomcb5tb2/questions
Outc0SF
"""


class Node:

	def __init__(self, value=None):
		self.data = value
		self.next = None


def generateLinkedList(lst):

	head = Node(lst[0])
	curr = head	
	for i in range(1, len(lst)):
		curr.next = Node(lst[i])
		curr = curr.next
	
	return head

def printForward(head):
	
	while head:
		print(head.data)
		head = head.next
	
def printBackward(head):
	
	if not head:
		return
		
	printBackward(head.next)
	print(head.data)


"""
input:
1	->	5	->	7	->	10
output:
1	<-	5	<-	7	<-	10

prev	curr	temp
none	1	->	5	->	7	->	10

while curr.next:
	temp = curr.next
	curr.next = prev
	prev = curr
	curr = temp


"""

def reverse(head):

	prev = None
	curr = head
	
	while curr.next:
		temp = curr.next
		curr.next = prev
		pre = curr
		curr = temp
		
	return prev
	
	

def reverseRecur(node):

	pass

"""

swap(head,5,12)

input
1	->	5	->	7	->	10	->	12	->	15	->	None
output
1	->	12	->	7	->	10	->	5	->	15	->	None

			
			p_a		node_a			p_b		node_b	
dummy	->	1	->	5	->	7	->	10	->	12	->	15	->	None
dummy	->	1	->	5	->	7	->	10		12		15	->	None
dummy	->	1		5		7	->	10		12		15	->	None
dummy	->	1	->	12	->	7	->	10	->	5	->	15	->	None





"""

	
def swap(head,a,b):
	
	dummy = Node()
	dummy.next = head
	
	p_a, node_a, p_b, node_b = None, None, None, None
	p = head
	
	while p:
		
		if p.next and p.next.data == a:
			p_a = p
			node_a = p.next
			
		if p.next and p.next.data == b:
			p_b = p
			node_b = p.next
			
		p = p.next
			
	if not node_a or not node_b:
		return head
	
	#save
	tnb = node_b.next
	p_a.next = node_b
	node_b.next = node_a.next
	node_a.next = tnb
	p_b.next = node_a


	
	return dummy.next
	
def isCircular(head):

	circular = False

	p_1_step = head
	p_2_steps = head
	
	while p_1_step.next:
	
		p_1_step = p_1_step.next

		if p_2_steps.next:
			p_2_steps = p_2_steps.next		
		if p_2_steps.next:
			p_2_steps = p_2_steps.next		
			
		if p_2_steps and p_1_step.data = p_2_steps.data:
			circular = True
			break
			
	return circular
	
if __name__ == "__main__":
	lst = [1,5,7,10,12,15]
	head = generateLinkedList(lst)
	
	#printForward(head)
	#printBackward(head)
	
	head = swap(head,5,12)
	printForward(head)
	
	