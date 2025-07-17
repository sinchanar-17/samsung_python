t = int(input("Enter the number of text case : "))
for i in range(t):
    n = int(input("Enter the number of boys and girls : " ))
    g_arr = [int(input("Enter the height of girl :"))for i in range(0,n//2)]
    b_arr = [int(input("Enter the height of girl :"))for i in range(0, n//2)]
    g_arr.sort()
    b_arr.sort()
    final_arr = []
    for i in range(n):
        if b_arr[i] > g_arr[i]:
             if b_arr[i]>g_arr[i-1]:
                final_arr.append(b_arr[i])
                sorted = True
        else:
            if g_arr[i] > b_arr[i-1]:
                final_arr.append(g_arr[i])
                sorted =True
    print("The final line of boys and girls : ",final_arr)
    if sorted:
        print("YES")
        break
    else:
        print("NO")
        break

                             

    
 

                   