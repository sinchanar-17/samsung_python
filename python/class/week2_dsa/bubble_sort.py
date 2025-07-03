def bubble_sort(oranges):
    n = len(oranges)
    pivot = oranges[n - 1]
    k = 0
    for i in range(n - 1):
        if oranges[i] <= pivot:
            oranges[i], oranges[k] = oranges[k], oranges[i]
            k += 1
    oranges[k], oranges[n - 1] = oranges[n - 1], oranges[k]
    return oranges

# Inputs
random_input = [7, 2, 10, 5, 3, 12, 9, 6]
increasing_input = [1, 2, 3, 4, 5, 6, 7, 8]
decreasing_input = [15, 13, 10, 9, 6, 4, 3, 2]

print(bubble_sort(random_input[:]))
print(bubble_sort(increasing_input[:]))
print(bubble_sort(decreasing_input[:]))
