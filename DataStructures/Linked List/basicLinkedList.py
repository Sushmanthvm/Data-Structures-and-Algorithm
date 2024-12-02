class Node(object):
	"""docstring for Node"""
	def __init__(self, data,next):
		self.data = data
		self.next = next


if __name__ == '__main__':
	head = Node(1,None)
	temp=head
	for i in range(2,5):
		x = Node(i,None)
		temp.next = x 
		temp = temp.next

	temp = head

	while temp != None:
		print(temp.data, end=" ")
		temp=temp.next


