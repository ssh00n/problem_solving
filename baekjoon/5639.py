import sys
import time
sys.setrecursionlimit(10**6)

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def get_preindex():
    return construct_tree_util.preindex

def increment_preindex():
    construct_tree_util.preindex += 1

def construct_tree_util(pre, low, high):
    if low > high:
        return None
    
    # The first node in preorder traversal is root. so take
    # the node at preindex from pre[] and make it root
    # and increment preindex
    
    root = Node(pre[get_preindex()])
    increment_preindex()
    
    
    # if the current subarray has only one element
    # no need to recur
    if low == high:
        return root
    
    r_root = -1
    
    # search for the first element greater than root
    for i in range(low, high+1):
        if pre[i] > root.data:
            r_root = i
            break
    
    # If no elements are greater than the current root,
    # all elements are left children
    # so assign root appropriately
    if r_root == -1:
        r_root = get_preindex() + (high - low)
    
    # Use the index of element found in preorder to divide
    # preorder array in two parts. Left subtree and right subtree
    root.left = construct_tree_util(pre, get_preindex(), r_root-1)
    root.right = construct_tree_util(pre, r_root, high)
    return root

# The main function to construct BST from given preorder
# traversal. This function mainly uses constructTreeUtil()

def construct_tree(pre):
    size = len(pre)
    construct_tree_util.preindex = 0
    return construct_tree_util(pre, 0, size-1)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)
    

if __name__ == '__main__':
    pre = []
    
    while True:
        user_input = sys.stdin.readline().rstrip()
        if len(user_input) < 1:
            break
        pre.append(int(user_input))
        
    root = construct_tree(pre)
    post_order(root)