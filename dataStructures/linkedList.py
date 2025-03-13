#!/bin/python3
class linkedListItem:
	def __init__(self, val, next=None, prev=None):
		self.val=val
		self.next=next
		self.prev=prev

	def get_val(self):
		return val

	def link(self, next=None, prev=None):
		self.next=next
		self.prev=prev

	def step(self, counter):
		if counter==0:
			return self
		else:
			if counter<0:
				return self.previous.step(counter+1)
			elif counter>0:
				return self.next.step(counter-1)

# List is only linked forward. Traversing backward is impossible until it's linked backward.

i1=linkedListItem(4)

i2=linkedListItem(6)
i1.link(next=i2)

i3=linkedListItem(7)
i2.link(next=i3)

i4=linkedListItem(9)
i3.link(next=i4)

print(i1.step(3).val)
