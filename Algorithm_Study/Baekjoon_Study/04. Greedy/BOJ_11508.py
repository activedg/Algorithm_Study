import sys
inp = sys.stdin.readline
price = sorted([int(inp()) for _ in range(int(inp()))], reverse=True)
res = 0
for i, p in enumerate(price):
    if i % 3 != 2:
        res += p
print(res)

# left, right = 0, len(price) - 1
# res = 0
# while left <= right:
#     res += price[left]
#     if left + 2 <= right:
#         res += price[right-1]
#         left += 1
#         right -= 2
#     elif left == right:
#         break
#     else:
#         res += price[right]
#         left += 1
#         right -= 1
# print(res)