
def inorder(root):
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__ == '__main__':
    root = 1
    inorder(root)