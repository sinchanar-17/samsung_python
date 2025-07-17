n_array, x_part, y_part = map(int, input("Enter total number of elements in array, number of elements in x and y such that x + y = n: ").split())

if x_part + y_part == n_array:
    array_list = []
    print(f"Enter {n_array} elements of the array: ")
    for _ in range(n_array):
        array_list.append(int(input()))

    array_list.sort(reverse = True)

    p_element = array_list[x_part - 1] - array_list[x_part] - 1

    print(p_element, "elements satisfies the condition!!")
else:
    print("x and y value does not match!!")