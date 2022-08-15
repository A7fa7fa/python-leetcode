from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	
	def rec(self, node, prev, head):
		
		if node.next is not None:
			head = self.rec(node.next, node, head)
		else:
			head = node
			
		node.next = prev
		return head

	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		
		
		if not head or not head.next:
			return head
		
		return self.rec(head, None, head)



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
res = s.reverseList(head)
print(res.val)