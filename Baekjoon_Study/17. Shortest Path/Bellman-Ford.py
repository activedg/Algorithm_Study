import sys
inp = lambda : sys.stdin.readline()
INF = sys.maxsize
def bf(start):
    dist[start] = 0
    # 전체 n번 라운드 반복
    for i in range(n):
        # 매 반복마다 "모든 간선" 확인
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False
# 노드의 개수, 간선의 개수
n, m = 5, 8
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = [[1, 2, 7],
         [1, 3, 5],
         [1, 4, 3],
         [3, 4, 3],
         [3, 5, 3],
         [5, 3, 2],
         [4, 5, -6],
         [4, 2, 3]]
# 최단 거리 테이블 모두 무한으로 초기화
dist = [INF] * (n + 1)
# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    # 1번 노드 제외하고 출력
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])