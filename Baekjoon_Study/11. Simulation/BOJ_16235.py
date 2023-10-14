import sys
inp = lambda : sys.stdin.readline()
# NxN 크기의 땅
# 처음 양분에 모든 칸에 5
# M개의 나무 구매해 땅에 심음, 한 칸에 여러 개의 나무 심어져 있을 수 있음
# 1. 봄 : 나무가 자신의 나이만큼 양분을 먹고 나이 1 증가/ 나이가 어린 나무부터 양분 먹음
## 양분 부족해서 자신의 나이만큼 먹을 수 없으면 즉시 죽음
# 2. 여름 : 봄에 죽은 나무가 양분으로 변함. 죽은 나무 나이 // 2
# 3. 가을 : 나무 번식(나이 5의 배수), 인접한 8개 칸에 나이가 1인 나무 생김
# 4. 겨울 : S2D2 땅 돌아다니면서 양분 추가
N, M, K = map(int, inp().split())
A = [[0] * N for _ in range(N)]
for i in range(N):
    temp = list(map(int, inp().split()))
    for j in range(len(temp)):
        A[i][j] = temp[j]
tree = [[[] for _ in range(N)] for _ in range(N)]
nutrition = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, inp().split())
    tree[x-1][y-1].append(z)
def spring():
    dead, rise = [], []
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) == 0: continue

            nut_temp = nutrition[i][j]
            tree_temp = []

            tree[i][j].sort()
            for k in range(len(tree[i][j])):
                if nut_temp < tree[i][j][k]:
                    # 여름에 줄 양분
                    dead.append((i, j, tree[i][j][k] // 2))
                else:
                    nut_temp -= tree[i][j][k]
                    tree_temp.append(tree[i][j][k] + 1)
                    if not (tree[i][j][k] + 1) % 5:
                        rise.append((i, j))
            nutrition[i][j] = nut_temp
            tree[i][j] = tree_temp
    return dead, rise

def summer(arr: list):
    for i, j, k in arr:
        nutrition[i][j] += k
def autumn(arr: list):
    for x, y in arr:
        for dx in range(-1, 2):
            nx = x + dx
            if nx < 0 or nx >= N: continue
            for dy in range(-1, 2):
                ny = y + dy
                if nx == x and ny == y: continue
                if ny < 0 or ny >= N: continue
                tree[nx][ny].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += A[i][j]

for _ in range(K):
    dead, rise = spring()

    summer(dead)

    autumn(rise)

    winter()

res = 0
for i in range(N):
    for j in range(N):
        res += len(tree[i][j])
print(res)
