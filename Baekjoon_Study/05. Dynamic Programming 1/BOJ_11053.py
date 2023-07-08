import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
A = list(map(int, inp().split()))
# dp = [1 for _ in range(N)]
# # 무조건 2차원 배열로 해야한다는 생각을 버리고, 자신 index까지 반복을 다시 돌리면서 생
# for i in range(1, N):
#     # 0 ~ i-1 까지 돌면서 작은 값 있는지 확인
#     for j in range(i):
#         # 자기 보다 작은 j번째 dp + 1
#         if A[i] > A[j]:
#             dp[i] = max(dp[j] + 1, dp[i])
# print(max(dp))

# 스택으로 풀기
stack = [A[0]]
for i in range(1, N):
    # 스택의 top보다 큰 경우 append
    if stack[-1] < A[i]:
        stack.append(A[i])
    else:
        for j in range(len(stack)):
            if A[i] <= stack[j]:
                stack[j] = A[i]
                break
print(len(stack))