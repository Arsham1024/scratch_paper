
class node():
    def __init__(self, val=0 , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class tree():
    def __init__(self, values):
        self.root = node(val=values[0])
        self.values = values



if __name__ == '__main__':
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    T = tree(values)