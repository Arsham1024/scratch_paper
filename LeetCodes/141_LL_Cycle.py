# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        itr = head

        while itr:
            if itr.val != -math.inf:
                itr.val = -math.inf
                itr = itr.next

            elif itr.val == -math.inf:
                return True

        return False