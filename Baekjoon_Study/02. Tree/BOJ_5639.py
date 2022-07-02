import sys
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline
bst = []
while True:
    try:
        bst.append(int(inp()))
    except:
        break
def post_order(left, right):
    if left >= right:
        return
    root = bst[left]
    if bst[right-1] <= root:
        post_order(left+1, right)
        print(root)
        return
    for t in range(left + 1, right):
        if root < bst[t]:
            div = t
            break
    post_order(left+1, div)
    post_order(div, right)
    print(root)

post_order(0, len(bst))
