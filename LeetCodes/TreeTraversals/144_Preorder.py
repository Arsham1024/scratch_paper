
def pre(root):
    print(root.val)
    pre(root.left)
    pre(root.right)

if __name__ == '__main__':
    pre(root)