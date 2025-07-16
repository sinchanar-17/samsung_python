initial_player = int(input("Enter initial player ID: "))
n = int(input("Enter number of passes: "))
player_list = [initial_player]
for i in range(n):
    command = input("Enter pass command: ")
    if command[0] == 'P':
        i, player_id = command.split()
        player_list.append(int(player_id))
    elif command[0] == 'B':
        if len(player_list) > 1:
            player_list.pop()
print("Player with ball:", player_list[-1])