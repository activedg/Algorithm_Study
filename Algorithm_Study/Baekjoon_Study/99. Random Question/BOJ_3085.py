import sys, bisect
inp = lambda : sys.stdin.readline()
a = [5, 17, 6]
b = [3, 9 , 13]
for t in a:
    print(bisect.bisect_left(b, t))