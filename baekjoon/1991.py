import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node): 
    print(node.data, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

# 자기 자신을 중간 순서에 방문
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inorder(tree[node.right])
    
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.data, end='')

tree = {}
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    data, left, right = input().split()
    # print(data, left, right)
    tree[data] = Node(data, left, right)
# for i in range(n):
#     data, left_node, right_node = input().split()
#     if left_node == ".":
#         left_node = None
#     if right_node == ".":
#         right_node = None
#     tree[data] = Node(data, left_node, right_node)
    
# print(tree.items())

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])



