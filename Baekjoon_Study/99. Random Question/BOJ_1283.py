import sys
from collections import defaultdict
inp = lambda : sys.stdin.readline().rstrip()
# 한 개 또는 여러 갠의 단어로 옵션 기능 설명
# 대표 알파벳 지정
## 하나의 옵션에 대해 왼쪽부터 오른쪽 순서로 단어의 첫 글자 이미 단축키로 지정되어있는지 확인
## 모든 단어의 첫글자 지정되어 있다면 왼쪽에서 부터 알파벳 지정
## 아무것도 지정 못하면 스킵
shortcuts = defaultdict(bool)
N = int(inp())
words = [[] for _ in range(N)]
for i in range(N):
    word = inp()
    check = False

    word_temp = list(word.split())
    for j in range(len(word_temp)):
        # 단어 첫 글자부터 확인
        words[i].append(word_temp[j])

        w = word_temp[j][0]
        if not check and not shortcuts[w.lower()]:
            shortcuts[w.lower()] = True
            check = True
            words[i][j] = words[i][j].replace(w, "[" + w + "]", 1)

    if not check:
        for j in range(len(word_temp)):
            for w in word_temp[j][1:]:
                if not shortcuts[w.lower()]:
                    shortcuts[w.lower()] = True
                    words[i][j] = words[i][j].replace(w, "[" + w + "]", 1)
                    check = True
                    break
            if check: break

for word in words:
    print(' '.join(word))