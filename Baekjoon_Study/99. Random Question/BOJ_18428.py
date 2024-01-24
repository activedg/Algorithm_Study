import sys
from itertools import combinations

inp = lambda: sys.stdin.readline()
# 특정 위치에는 선생님, 학생, 혹은 장애물, 몇 명 학생들 몰래 복도로 나옴
# 선생님 : 상, 하, 좌, 우 방향에 대하여 다 봄, 장애물 뒤에는 안보임
## 선생님 T, 학생 S, 장애물 O
# 정확히 3개의 장애물을 설치
N = int(inp())

# 1. 전체 빈 칸 중 3개 고르기?
T, S, X = [], [], []
maps = []
for i in range(N):
    temp = list(map(str, inp().split()))
    maps.append(temp)
    for j in range(N):
        if temp[j] == "T":
            T.append((i, j))
        elif temp[j] == "S":
            S.append((i, j))
        else:
            X.append((i, j))
res = False

def check_possible(students, teachers, obs):
    for t in teachers:
        for s in students:
            # 상하 좌우 방향 중에서 겹치는 경우
            if t[0] == s[0] or t[1] == s[1]:
                check = False
                for o in obs:
                    # 장애물의 i 좌표가 같거나 j 좌표가 같아야 함
                    if (o[0] == t[0] == s[0] and min(t[1], s[1]) < o[1] < max(t[1], s[1])) or (o[1] == t[1] == s[1] and min(t[0], s[0]) < o[0] < max(t[0], s[0])):
                        check = True
                        break
                if not check: return False
    return True

res = False
for obstacles in list(combinations(X, 3)):
    if check_possible(S, T, obstacles):
        res = True
        break
    # for oi, oj in obstacles:
    #     maps[oi][oj] = "O"
    # # 학생의 상하좌우를 확인해보기
    # check = True
    # for si, sj in students:
    #     for k in range(4):
    #         if not check: break
    #
    #         ni, nj = si + dx[k], sj + dy[k]
    #         while 0 <= ni < N and 0 <= nj < N:
    #             if maps[ni][nj] == "O":
    #                 break
    #             elif maps[ni][nj] == "T":
    #                 check = False
    #                 break
    #             ni, nj = ni + dx[k], nj + dy[k]
    # if check:
    #     res = True
    #     break
    #
    # for oi, oj in obstacles:
    #     maps[oi][oj] = "X"
print("YES" if res else "NO")
