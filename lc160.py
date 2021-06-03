# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# a + common + b = b + common + a
# double ptr
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA = headA
        ptrB = headB
        trial = 0
        while ptrA != ptrB:
            if ptrA != None:
                ptrA = ptrA.next
            else:
                ptrA = headB

            if ptrB != None:
                ptrB = ptrB.next
            else:
                ptrB = headA

        return ptrA