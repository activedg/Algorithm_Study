from collections import defaultdict
import sys
# 크기가 N x N인 격자에 파이어볼 M개
inp = lambda : sys.stdin.readline().split()
# 모든 파이어볼이 자신의 방향 di로 속력 si 칸 만큼 이동
# 이동 끝난 후, 2개 이상 파이어볼 있는 칸에서 해당 사항 적용
# 1번 열은 N번 열과, 1번 행은 N번 행과 연결
## 모두 하나로 합쳐짐
## 4개의 파이어볼로 나누어짐
## 나누어진 파이어볼 질량, 속력, 방향 적용
## 질량 0인 파이어볼 소멸
N, M, K = map(int, inp())
boards = defaultdict(list)
for _ in range(M):
    temp = list(map(int, inp()))
    boards[(temp[0]-1, temp[1]-1)].append((temp[2], temp[3], temp[4]))
# 방향에 따른 인덱스
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    temp = defaultdict(list)
    for key, val in boards.items():
        for info in val:
            nx, ny = (key[0] + dx[info[2]] * info[1]) % N, (key[1] + dy[info[2]] * info[1]) % N
            temp[(nx, ny)].append(info)

    for key, val in temp.items():
        if len(val) >= 2:
            m_temp, s_temp = 0, 0
            cnt = len(val)
            temp_dir = val[0][-1] % 2
            check = True
            for info in val:
                if check and temp_dir != info[2] % 2:
                    check = False
                m_temp += info[0]
                s_temp += info[1]

            # 네 개로 나눈다
            m_temp = m_temp // 5
            s_temp = s_temp // cnt

            temp[key].clear()

            # 질량이 0이면 소멸
            if not m_temp: continue

            temp_list = (0, 2, 4, 6) if check else (1, 3, 5, 7)

            for t in temp_list:
                temp[key].append([m_temp, s_temp, t])
    boards = temp

res = 0
for val in boards.values():
    for info in val:
        res += info[0]
print(res)
