# psum => prefix 다 더한것
# beauty : psum[0] - psum[1] + psum[2] -psum[3] + ... (-1) ** (n-1) psum[n-1]
## arr이 재정렬 될 수 있으면 beauty of psum의 최대 가능 밸류 찾기

## n = 5
## arr = [3, 4, 5, 1 ,1]

# 모든 원소 다 받아서 정렬, 가장 작은 원소 순으로 들어가기

def getMaxBeauty(arr):
    # 작은 순서대로 정렬
    arr.sort()
    # 투 포인터로 돌면서, 맨 뒤 -> 맨 앞 순서 대로 넣기
    start, end = 0, len(arr) - 1
    arr_s = []
    while start <= end:
        if start == end:
            arr_s.append(arr[start])
            break

        arr_s.append(arr[end])
        arr_s.append(arr[start])
        start, end = start + 1, end - 1

    # psum 구하기
    psum = arr_s
    for i in range(1, len(arr_s)):
        psum[i] += psum[i-1]

    res = 0
    for j in range(len(psum)):
        if j % 2: res -= psum[j]
        else: res += psum[j]
    return res
print(getMaxBeauty([3,1,5,1,4]))