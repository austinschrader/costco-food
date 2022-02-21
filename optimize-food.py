import bisect

def minAbsDifference(nums, goal):
    n = len(nums)
    half = len(nums) // 2
    sums = {0}
    for i in range(half, n):
        for s in list(sums):
            sums.add(nums[i] + s)
    sums = sorted(sums)

    sums2 = {0}
    for i in range(half):
        for s in list(sums2):
            sums2.add(nums[i] + s)

    mn = 10 ** 9
    for s2 in sums2:
        ind = bisect.bisect_left(sums, goal - s2)

        if ind != len(sums):
            mn = min(mn, sums[ind] + s2 - goal)
        if ind != 0:
            mn = min(mn, goal - sums[ind - 1] - s2)
    print(sums)
    return mn

print(minAbsDifference([180,360,420], 1500))