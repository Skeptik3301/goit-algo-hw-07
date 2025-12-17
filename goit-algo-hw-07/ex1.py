class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_max(root):
    if root is None:
        return None
    
    current = root
    while current.right:
        current = current.right
    return current.val

root = Node(20)
insert(root, 11.3)
insert(root, 12)
insert(root, 40)
insert(root, 40.123)

print(find_max(root))