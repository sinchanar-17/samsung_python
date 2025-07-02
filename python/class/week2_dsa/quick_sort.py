def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    k = low
    for i in range (low, high):
        if arr[i] < pivot:
            arr[i], arr[k] = arr[k], arr[i]
            k +=1 
        arr[k + 1], arr[high] = arr[high], arr[k + 1]
        

random_input = [7, 2, 10, 5, 3, 12, 9, 6]
increasing_input = [1, 2, 3, 4, 5, 6, 8, 7]
decreasing_input = [15, 13, 10, 9, 6, 4, 3, 2]

print(random_input)
print(increasing_input)
print(decreasing_input)

