import copy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #print(self.makeArrayFromList(head,[]))
        current = head
        if(current is not None):
            if(current.next is not None):
                while(current.next.next is not None):
                    current = current.next
                current.next.next = head.next
                for_attachment_to_head = current.next
                head.next = for_attachment_to_head
                current.next = None
                if(head.next is None):
                    head.next = for_attachment_to_head
                    for_attachment_to_head.next = None
                elif(head.next.next is not None):
                    print(head.next.next.val)
                    self.reorderList(head.next.next)

    def makeArrayFromList(self,head,array):
        array.append(head.val)
        if(head.next is not None):
            self.makeArrayFromList(head.next,array)
        return array

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
Solution().reorderList(list)
print(Solution().makeArrayFromList(list,[]))
