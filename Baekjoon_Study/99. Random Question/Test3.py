# pnl[i] : i번째 월의 수입(음수 가능)
# 연속되는 배열의 합중 최대, 단 길이는 K를 넘기면 안됨
import sys
def getMaxProfit(pnl, k):
    sub = [[] for _ in range(len(pnl))]
    # 리스트로 다 만들기
    sub[0] = [pnl[0]]
    res = pnl[0]

    for i in range(1, len(pnl)):
        # 직전 sub가 길이가 k보다 작은 경우
        if len(sub[i-1]) < k:
            temp = sum(sub[i-1])
            if temp <= 0:
                sub[i] = [pnl[i]]
            else:
                sub[i] = sub[i-1]
                sub[i].append(pnl[i])
        # 직전 sub 길이가 k
        else:
            temp = sum(sub[i-1])
            if temp <= 0:
                sub[i] = [pnl[i]]
            else:
                sub[i] = sub[i-1][1:]
                sub[i].append(pnl[i])
        res = max(res, sum(sub[i]))
    return res
def getMaxProfit(pnl, k):
    sub = []
    # 리스트로 다 만들기
    res = pnl[0]

    for i in range(1, len(pnl)):
        # 직전 sub가 길이가 k보다 작은 경우
        current_sum = sum(sub)
        res = max(res, current_sum)
        if len(sub) < k:
            if current_sum < 0:
                sub = [pnl[i]]
            else:
                sub.append(pnl[i])
        # 직전 sub 길이가 k
        else:
            if current_sum <= 0:
                sub = [pnl[i]]
            else:
                sub.pop(0)
                sub.append(pnl[i])
    return max(0, res, sum(sub))