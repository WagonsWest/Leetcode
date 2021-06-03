# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# 递归
def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None

    return p
    