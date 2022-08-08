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

    def middleNode2(self, head):
        length = 0 # keeps track of total length of nodes
        middle = head #keeps track of middle node
        while head: # as long there is a head
            head = head.next # move forward
            length += 1 # up length by one
            
            if length % 2 == 0: # whenever new length is devisible by 2. half of length has to move forward as well. every two steps of head, middle mmoves es well
                middle = middle.next
        
        return middle
        

if __name__ == "__main__":
    l = ListNode()
    head = l
    for i in range(1, 10):
        l.next = ListNode(i)
        l = l.next
    print(l.middleNode(head).val)