# 숫자 1 부터 n까지
# endNode 수 m개
# endNode[i] ~ endNode[i+1] 사이의 노드는 다 방문
# 가장 많이 방문한 노드는? 여러개면 번호 작은순
def circularArray(n, endNode):
    cnt = [[0, i] for i in range(n+1)]
    for i in range(len(endNode) - 1):
        start, end = endNode[i], endNode[i+1]
        if start > end:
            for j in range(end, start + 1):
                cnt[j][0] += 1
        else:
            for j in range(start, end + 1):
                cnt[j][0] += 1
    # 정렬
    cnt.sort(key=lambda x:(-x[0], x[1]))
    return cnt[0][1]
print(circularArray(10, [10, 5, 8, 2, 7, 9, 10]))