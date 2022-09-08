import sys
sys.setrecursionlimit(10**8)
inp = lambda : sys.stdin.readline()
N = int(inp())
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
nodes = {}
for _ in range(N):
    a, b, c = map(int, inp().split())
    nodes[a] = Node(a, b, c)
count = 0
inorder_path = []
def inorder(node: Node):
    if node.left != -1:
        inorder(nodes[node.left])
    inorder_path.append(node)
    if node.right != -1:
        inorder(nodes[node.right])
def s_inorder(node: Node):
    global count
    if node.left != -1:
        s_inorder(nodes[node.left])
        count += 1
    if node == inorder_path[-1]:
        print(count)
        exit()
    count += 1
    if node.right != -1:
        s_inorder(nodes[node.right])
        count += 1
inorder(nodes[1])
s_inorder(nodes[1])