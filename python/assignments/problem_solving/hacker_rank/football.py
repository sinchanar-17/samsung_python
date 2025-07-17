test_cases = int(input("Enter number of test cases: "))
number_of_passes, ID = map(int, input("Enter number of passes and player ID who has the ball: ").split())

for _ in range(test_cases):
    ball = []
    print("Enter the tyoe of pass you want to perform (P ID(Player ID whom you want to pass) or B (Back)): ")
    for _ in range(number_of_passes):
        passes = input()
        if passes == "B":
            ball.append(ball[-2])
        else:
            p, id = passes.split()
            ball.append(int(id))

    print("Player", ball[-1])