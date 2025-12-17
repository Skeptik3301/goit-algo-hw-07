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

def find_min(root):
    if root is None:
        return None
    
    current = root
    while current.left:
        current = current.left
    return current.val

root = Node(20)
insert(root, 10)
insert(root, 12.3)
insert(root, 100)
insert(root, 0.3301)

print(find_min(root))