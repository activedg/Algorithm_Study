import sys
inp = lambda : sys.stdin.readline().split()
N, K = map(int, inp())
# 수열 S에서 최대 K 번의 숫자를 삭제 한 수열에서 얻을 수 있는 가장 긴 부분 수열
S = list(map(int, inp()))
end, cnt = 0, 0
res = 0
temp = 0
for i in range(N):
    while cnt <= K and end < N:
        # end 포인터가 가리키는 숫자가 홀수
        if S[end] % 2:
            cnt += 1
        else:
            temp += 1
        end += 1

        if i == 0 and end == N:
            res = temp
            break
    if cnt == K + 1:
        res = max(res, temp)
    # 시작 포인터가 홀수인 경우 값 빼기
    if S[i] % 2:
        cnt -= 1
    else:
        temp -= 1

print(res)