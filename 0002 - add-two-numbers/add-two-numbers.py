# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		
		l1DigitsStr = ""
		l2DigitsStr = ""
		
		while l1:
			l1DigitsStr = f"{l1.val}{l1DigitsStr}"
			l1 = l1.next
		while l2:
			l2DigitsStr = f"{l2.val}{l2DigitsStr}"
			l2 = l2.next
			
		sumOfDigist = int(l1DigitsStr) +int(l2DigitsStr)
		
		result = None
		head = None
		for digit in reversed(str(sumOfDigist)):
			if result is None:
				result = ListNode(digit)
				head = result
			else:
				result.next = ListNode(digit)
				result = result.next
		
		return head



if __name__ == "__main__":
	node3 = ListNode(3)
	node2 = ListNode(4)
	node1 = ListNode(2)
	node1.next = node2
	node2.next = node3

	bnode3 = ListNode(4)
	bnode2 = ListNode(6)
	bnode1 = ListNode(5)
	bnode1.next = bnode2
	bnode2.next = bnode3

	sol = Solution()
	res = sol.addTwoNumbers(node1, bnode1)
	print(res)