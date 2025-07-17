#Harry and sorceror's problem
def harry_sorceror():
    n = int(input("Enter the number of gold coins in Harry's Bag : "))
    values = list(map(int, input(f"Enter any {n} separated values of gold coins: ").split()))
    q, x = map(int, input("Enter the number of instructions and worth of gold coins in monk's bag: ").split())
    monk_bag = []
    number_of_coins = 0
    for i in range(0, int(q)):
        instruction =input("Enter the instruction you want to give Harry or Remove : ")
        if instruction == "Harry":
            if number_of_coins < n:
                monk_bag.append(values[number_of_coins])
                number_of_coins += 1
        elif instruction == "Remove":
            if monk_bag:
                monk_bag.pop()
        if sum(monk_bag) == x:
                print(len(monk_bag))
                return
    print(-1)
harry_sorceror()