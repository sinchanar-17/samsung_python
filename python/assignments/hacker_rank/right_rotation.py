
def isSameReflection():
    original_str = input("Enter the original string: ")
    rotated_str = input("Enter the rotated string: ")

    temp_str = rotated_str + rotated_str
    
    if original_str in temp_str:
        return 1
    else:
        return -1
    
reply = isSameReflection()
print(reply)