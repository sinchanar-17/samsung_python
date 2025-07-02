def binary_search_do_while(arr, target):
    low = 0 
    high = len(arr) - 1

    while True:
        if low > high:
            return -1
        
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

arr = [10, 20, 30, 40, 50, 60, 70]
target = 60
index = binary_search_do_while(arr, target)
if index != -1:
    print("target foud at index",index)
else:
    print("target not found")