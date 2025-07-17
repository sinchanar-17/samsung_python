#Sum of even and odd indices(main question yahi hai pure scenerio mai se)
N = [45, -13, -30, -10, 50, 35, -5, 5, 8]
memory_allocation = 0  #sum of even indices
memory_deallocation = 0 #sum of odd indices
for i in range (len(N)):
    if i % 2 == 0:
        memory_allocation += N[i]
    else:
        memory_deallocation += N[i]
        
print(memory_allocation)
print(memory_deallocation)


''' optimal version
N = [45, -13, -30, -10, 50, 35, -5, 5, 8]

sum_even_idx = sum(N[i] for i in range(0, len(N), 2))
sum_odd_idx = sum(N[i] for i in range(1, len(N), 2))

print("Sum of elements at even indices:", sum_even_idx)
print("Sum of elements at odd indices:", sum_odd_idx)

'''