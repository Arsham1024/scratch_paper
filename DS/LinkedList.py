from random import random


class Node:
    def __init__(self, data=None , next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def inset_at_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        string = ''
        itr = self.head
        if itr:
            while itr:
                string += str(itr.data) + "-->"
                itr = itr.next
            print(string)
        else:
            return "No Head"


if __name__ == "__main__":
    ll = LinkedList()
    ll.inset_at_head(1)
    rand = round(random()*100%100, 2)
    for i in range(1,50):
        ll.inset_at_head(rand)

    ll.print()
