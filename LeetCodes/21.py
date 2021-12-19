# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



if __name__ == "__main__":
    list = []
    list2 = []

    for i in range(0, 500, 2):
        list.append(ListNode(i , i+2))

    for i in list:
        print(i.val , i.next)


