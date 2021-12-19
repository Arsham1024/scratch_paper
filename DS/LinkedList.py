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

    def insert_at_end(self, data):
        node = Node(data, None)

        if not self.head:
            self.head = node
            return

        else:
            itr = self.head
            while(itr.next):
                itr = itr.next

            itr.next = node

    def remove(self,index):
        if index >= self.length() or index < 0:
            raise Exception("Not a valid index")

        itr = self.head

        if index == 0:
            self.head = itr.next
            return

        i = 0
        temp = 0
        while itr:
            if i == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            i += 1


    # Helper print method
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

    def length(self):
        count = 0
        node = self.head

        if not self.head:
            return 0
        elif not node.next:
            return 1

        else:
            while(node):
                count +=1
                node = node.next
            return count



if __name__ == "__main__":
    ll = LinkedList()
    ll.inset_at_head(1)

    for i in range(1,15):
        rand = round(random() * 100 % 100, 2)
        ll.inset_at_head(rand)

    ll.insert_at_end("This is the end, hold your breath and count to ten...")
    ll.print()

    ll.remove(1)

    ll.print()

    print(ll.length())
