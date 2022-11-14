import sys
from collections import defaultdict
inp = lambda : sys.stdin.readline()
R, C = map(int, inp().split())
# 위에서 아래로 읽기
word_list = [inp() for _ in range(R)]
start, end = 0, R-1
## 한 번 문자열이 중복되면 계쏙 중복된다는 점 이용 -> 이분 탐색 활용
result = 0
# 이분 탐색 시 start, end 같을 수 있는지 여부 판단 필요
while start <= end:
    mid = (start + end) // 2
    word_dict = defaultdict(int)
    check = True
    for j in range(C):
        temp = ''
        for i in range(mid, R):
            temp += word_list[i][j]
        if word_dict[temp] == 1:
            check = False
            break
        word_dict[temp] += 1
    if check:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
# words = []
# for j in range(C):
#     temp = ''
#     for i in range(R):
#         temp += word_list[i][j]
#     words.append(temp)
# # 단어 C개 생성
# ## 중복 여부 판단 하기 -> Set 으로 하기
# word_set = set()
# res = 0
# for i in range(1, R):
#     word_set.clear()
#     for j in range(C):
#         word_set.add(words[j][i:])
#     if len(word_set) == C: res += 1
# print(res)
