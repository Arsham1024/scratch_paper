
def post(root):
    post(root.left)
    post(root.right)
    print(root.val)

if __name__ == '__main__':
    post(root)