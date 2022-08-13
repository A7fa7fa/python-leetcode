from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	
	if not list1:
		return list2
	if not list2:
		return list1
	if not list1 and not list2:
		return None
	
	if list2.val < list1.val:
		list1, list2 = list2, list1
	
	head = list1
	
	while list1 and list2:
			
			# end of list1 so append list2 and return head
			if not list1.next:
				list1.next = list2
				return head
			
			# next value of list2 is smaller than currecnt head of list2 so move one forward
			if list1.next.val < list2.val:
				list1 = list1.next
			# else 
			else:
				list2, list1.next = list1.next, list2
				list1 = list1.next
		
	return head
			
			
			