# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head != None and head.val == val:
            head = head.next

        if head == None:
            return head

        prev = head
        res = head
        while head != None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return res
