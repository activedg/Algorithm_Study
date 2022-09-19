import sys
inp = lambda : sys.stdin.readline()
# def search(arr: list, target: int):
#     gap_min, cnt = sys.maxsize, 0
#     ## -7 -4 -3 -2 0 1 2 5 9 12
#     for i in range(len(arr)):
#         s, e = i + 1, len(arr) - 1
#         while s <= e:
#             mid = s + (e - s) // 2
#             t = arr[i] + arr[mid]
#             gap = abs(t - target)
#             if t > target:
#                 e = mid - 1
#             else:
#                 s = mid + 1
#             if gap < gap_min:
#                 gap_min = gap
#                 cnt = 1
#             elif gap == gap_min:
#                 cnt += 1
#     return cnt
# for _ in range(int(inp())):
#     n, k = map(int, inp().split())
#     print(search(sorted(map(int, inp().split())), k))
def search(arr: list, target: int):
    s, e = 0, len(arr) - 1
    _min = sys.maxsize
    cnt = 1
    while s < e:
        val = arr[s] + arr[e]
        val_abs = abs(val - target)
        if _min > val_abs:
            cnt = 1
            _min = val_abs
        elif _min == val_abs:
            cnt += 1
        if val > target:
            e -= 1
        else:
            s += 1
    return cnt
for _ in range(int(inp())):
    n, k = map(int, inp().split())
    print(search(sorted(map(int, inp().split())), k))