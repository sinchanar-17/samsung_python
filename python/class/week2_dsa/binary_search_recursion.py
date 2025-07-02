def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

arr = [10, 20, 30, 40, 50, 60, 70]
target = 95
index = binary_search_recursive(arr, target, 0, len(arr) - 1)
if index != -1:
    print("target foud at index",index)
else:
    print("target not found")