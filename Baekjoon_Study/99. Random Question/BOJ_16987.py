import sys
inp = lambda : sys.stdin.readline()
# 최대한 많은 계란 깨기
# 가장 왼쪽 계란 들기 -> 깨지지 않은 다른 계란 중 하나 치기
## 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어가기
# 다음칸으로 가서 2번 반복
N = int(inp())
# 내구도, 무게 순
eggs = [list(map(int, inp().split())) for _ in range(N)]
## 부딪힌 계란의 무게만큼 내구도 감소
res = 0
## 계란 개수가 적고 딱히 그리디 한 방법 존재하지 않아서 백트래킹으로 해봄
# 배열 전달하지 말고 cnt 값으로 전달해서 계산해보기
def dfs(idx, cnt):
    if idx == N:
        global res
        res = max(res, cnt)
        return

    # 현재 달걀이 깨졌거나 나머지가 다 깨진 경우
    if eggs[idx][0] <= 0 or cnt == N - 1:
        dfs(idx+1, cnt)
        return

    else:
        for i in range(N):
            if idx == i: continue
            if eggs[i][0] > 0:
                eggs[i][0] -= eggs[idx][1]
                eggs[idx][0] -= eggs[i][1]
                if eggs[i][0] <= 0: cnt += 1
                if eggs[idx][0] <= 0: cnt += 1
                dfs(idx + 1, cnt)
                if eggs[i][0] <= 0: cnt -= 1
                if eggs[idx][0] <= 0: cnt -= 1
                eggs[i][0] += eggs[idx][1]
                eggs[idx][0] += eggs[i][1]

dfs(0, 0)
print(res)