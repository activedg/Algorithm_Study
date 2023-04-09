import sys
inp = lambda : sys.stdin.readline().split()
N, M, x, y, K = map(int, inp())
maps = [list(map(int, inp())) for _ in range(N)]
op = list(map(int, inp()))
# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 주사위 처음에 모든면 0
# 바깥으로 이동하려 하면 명령 무시, 출력도 x
# 주사위 이동할 때마다 윗면에 있는 숫자
## 주사위 이동한 칸에 0이 있으면 바닥면에 있는 숫자가 복사됨
## 0이 아니면 칸에 쓰여진 숫자가 바닥면으로 복사, 칸에 쓰여있는 숫자가 0으로 됨
# 위쪽면, 뒷면, 우측면, 왼쪽면, 앞면, 바닥면
#   2        6
# 4 1 3 -> 4 2 3
#   5        1
#   6        5
class Dice:
    up = 0
    down = 0
    front = 0
    behind = 0
    left = 0
    right = 0

    def roll(self, move):
        if move == 1:
            self.right, self.down, self.left, self.up = self.up, self.right, self.down, self.left
        elif move == 2:
            self.right, self.down, self.left, self.up = self.down, self.left, self.up, self.right
        elif move == 3:
            self.behind, self.up, self.front, self.down = self.up, self.front, self.down, self.behind
        else:
            self.behind, self.up, self.front, self.down = self.down, self.behind, self.up, self.front

dice = Dice()
for m in op:
    i = m - 1
    nx, ny = x + dx[i], y + dy[i]
    # 0 인경우 패스
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    dice.roll(m)
    if maps[nx][ny]:
        dice.down = maps[nx][ny]
        maps[nx][ny] = 0
    else:
        maps[nx][ny] = dice.down
    print(dice.up)
    x, y = nx, ny
