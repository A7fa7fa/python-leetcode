# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next and n == 1:
            return None

        count = 0

        temp = head

        # node to remove
        remove = head
        # node in front to remove node
        prev = None

        # traverse whole list
        while temp:            
            count += 1
            temp = temp.next

            # pointer to nodes is nth nodes behind temp
            # when temp is at the end of list
            # remove is nth node from the back
            if count > n:
                prev = remove
                remove = remove.next

        # head is the nth node so just return head.next
        if prev is None:
            return head.next

        # set prev next node to remove next node
        # that removes the node remove from list
        prev.next = remove.next

        return head