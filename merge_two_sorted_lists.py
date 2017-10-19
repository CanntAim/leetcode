# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        print(self.val)
        if(self.next is not None):
            self.next.display()

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = None
        if(l1.val <= l2.val and l1.next is not None):
            n = ListNode(l1.val)
            n.next = self.mergeTwoLists(l1.next,l2)
        elif(l1.val > l2.val and l2.next is not None):
            n = ListNode(l2.val)
            n.next = self.mergeTwoLists(l1,l2.next)
        elif(l1.val <= l2.val and l1.next is None):
            n = ListNode(l1.val)
            n.next = l2
        elif(l1.val > l2.val and l2.next is None):
            n = ListNode(l2.val)
            n.next = l1
        return n

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(8)
a4 = ListNode(9)
a5 = ListNode(10)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

b1 = ListNode(4)
b2 = ListNode(5)
b3 = ListNode(6)
b4 = ListNode(7)
b5 = ListNode(8)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5

solution = Solution()
m = solution.mergeTwoLists(a1,b1)
m.display()
