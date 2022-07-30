# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        
        temp = head
        result = [temp]
        while temp.next:
            result.append(temp.next)
            temp = temp.next
        
        return result[len(result) // 2]
        

if __name__ == "__main__":
    l = ListNode()
    head = l
    for i in range(1, 10):
        l.next = ListNode(i)
        l = l.next
    print(l.middleNode(head).val)