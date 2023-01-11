import sys
inp = lambda : sys.stdin.readline().split()
# [2 1 5 3 4]
nums = list(map(int, inp()))
compare = [i for i in range(1, 6)]
while True:
    for i in range(4):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums)
    if nums == compare:
        break