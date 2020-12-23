# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tick = False
        half = head
        while head:
            head = head.next
            if tick:
                half = half.next
            tick = not tick
        return half
