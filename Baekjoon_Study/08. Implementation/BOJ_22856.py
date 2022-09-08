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
## 중위 순회를 한 번 진행 하여 가장 마지막 진행 노드 파악
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
    ## 가장 마지막 방문 노드에서 exit
    if node == inorder_path[-1]:
        print(count)
        exit()
    count += 1
    if node.right != -1:
        s_inorder(nodes[node.right])
        count += 1
inorder(nodes[1])
s_inorder(nodes[1])