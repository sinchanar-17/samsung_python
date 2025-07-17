def subset_sum(arr, n, target):
    if target == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > target:
        return subset_sum(arr, n-1, target)
    return subset_sum(arr, n-1, target) or subset_sum(arr, n-1, target - arr[n-1])


print(subset_sum([3, 34, 4, 12, 5, 2], 6, 9))  # True
