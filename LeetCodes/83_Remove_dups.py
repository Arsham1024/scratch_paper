# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        start = head
        itr = head

        while itr:

            if itr.val == start.val:
                itr = itr.next

            elif itr.val != start.val:
                start.next = itr
                start = itr
                itr = itr.next

        start.next = None
        return head