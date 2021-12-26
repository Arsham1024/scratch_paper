# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #         basic for sure cases O(1)
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return list1

        #       pick the head as the smaller of two
        head = temp = ListNode()
        if list1.val <= list2.val:
            head = temp = ListNode(list1.val)
            list1 = list1.next
        else:
            head = temp = ListNode(list2.val)
            list2 = list2.next

        while list1 or list2:
            if not list1:
                temp.next = list2
                return head
            elif not list2:
                temp.next = list1
                return head

            elif list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next

            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        return head