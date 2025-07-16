for i in range(number_of_lines):
    print(" " * (number_of_lines - i), end="")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()