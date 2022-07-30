# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        temp = head
        while True:
            values.append(temp.val)
            if temp.next:
                temp = temp.next
                continue
            break
        for idx, value in enumerate(values):
            if values[-idx - 1] != value:
                return False
            if idx > len(values) /2:
                return True
        return True
                
            
            
        

if __name__ == "__main__":
    s = ListNode()
    print(s.isPalindrome(), s)