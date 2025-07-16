def optimized_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        sorted_flag = True
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                sorted_flag = False
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        if sorted_flag:
            break  # Stop early if already sorted
    return arr

arr = [3, 1, 4, 2, 5]
print("\nSorted array:", optimized_selection_sort(arr))
