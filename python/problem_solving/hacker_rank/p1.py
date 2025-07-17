def is_rotation(original_str, rotated_str):
    if len(original_str) != len(rotated_str):
        return -1
    temp_str = rotated_str * 2
    if original_str in temp_str:
        return 1
    else:
        return -1

original = input("Enter the original word: ")
rotated = input("Enter the rotated word: ")
result = is_rotation(original, rotated)
print(result)
