number_of_oranges = int(input("Enter the number of oranges plucked: "))

oranges = []
print("Enter the size of oranges: ")
for _ in range(number_of_oranges):
    oranges.append(int(input()))

k = 0

for i in range(len(oranges)):
    if oranges[i] <= oranges[len(oranges) - 1]:
        oranges[i], oranges[k] = oranges[k], oranges[i]
        k += 1

oranges[k], oranges[len(oranges) - 1] = oranges[len(oranges) - 1], oranges[k]

print(oranges)