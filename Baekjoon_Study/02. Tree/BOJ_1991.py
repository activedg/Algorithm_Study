import sys
N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    val, left, right = sys.stdin.readline().split()
    if left == '.': left = None
    if right == '.': right = None
    tree[val] = [left, right]

def inorder(c: chr):
    print(c, end='')
    if tree[c][0]: inorder(tree[c][0])
    if tree[c][1]: inorder(tree[c][1])

def preorder(c: chr):
    if tree[c][0]: preorder(tree[c][0])
    print(c, end='')
    if tree[c][1]: preorder(tree[c][1])

def postorder(c: chr):
    if tree[c][0]: postorder(tree[c][0])
    if tree[c][1]: postorder(tree[c][1])
    print(c, end ='')
inorder('A')
print('')
preorder('A')
print('')
postorder('A')
print('')