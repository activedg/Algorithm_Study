import sys
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
inp = lambda : sys.stdin.readline()
N = int(inp())
# 상어 초등학교에 교실 하나 있음, N x N 크기 격자
# 학생 수 N ^ 2
# 교실 가장 윗칸 (1, 1)!!!
# 학생의 순서를 정하고, 각 학생이 좋아하는 학생 4명 조사
# |r1 - r2| + |c1 - c2| = 1 -> 인접
## 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 정함
## 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
## 행의 번호가 가장 작은 칸
## 열의 번호가 가장 작은 칸
# 좌표에 대해 우선순위가 있음
# 우선순위로 앉을 칸 구하기

# 인접한 칸에 앉은 좋아하는 학생 수, 배치 데이터
student_map, student_data = {}, {}

# 학생 배치 순서
order = []
classroom = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N ** 2):
    inp_list = list(map(int, inp().split()))
    student_map[inp_list[0]] = inp_list[1:]
    order.append(inp_list[0])

def find_max(num):
    tmp = []
    for i in range(N):
        for j in range(N):
            if classroom[i][j]: continue
            # 좋아하는 사람 카운트
            like_cnt, empty_cnt = 0, 0
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if x < 0 or x >= N or y < 0 or y >= N: continue
                # 좋아하는 학생 번호에 있다면
                if classroom[x][y] in student_map[num]:
                    like_cnt += 1
                elif classroom[x][y] == 0:
                    empty_cnt += 1
            tmp.append((like_cnt, empty_cnt, i, j))
            ## 힙큐에 최대 힙으로 넣기
            # heapq.heappush(hq, (-like_cnt, -empty_cnt, i, j))
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))

    return tmp[0][2], tmp[0][3]
# 그 후 학생의 만족도 구한다
for o in order:
    data = find_max(o)
    student_data[o] = data
    classroom[data[0]][data[1]] = o

res = 0
for k in student_data.keys():
    x, y = student_data[k]
    like_cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        # 좋아하는 학생 번호에 있다면
        if classroom[nx][ny] in student_map[k]:
            like_cnt += 1
    if like_cnt == 0:
        res += 0
    elif like_cnt == 1:
        res += 1
    elif like_cnt == 2:
        res += 10
    elif like_cnt == 3:
        res += 100
    else:
        res += 1000
print(res)